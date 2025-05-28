from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Artigo, PedidoColaboracao
from .forms import ArtigoForm

class ArtigoDetailView(LoginRequiredMixin, DetailView):
    model = Artigo
    template_name = 'artigos/detalhe_artigo.html'

class ArtigoCreateView(LoginRequiredMixin, CreateView):
    model = Artigo
    form_class = ArtigoForm   
    template_name = 'artigos/form_artigo.html'
    success_url = reverse_lazy('lista_artigos')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ArtigoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Artigo
    form_class = ArtigoForm  
    template_name = 'artigos/form_artigo.html'
    success_url = reverse_lazy('lista_artigos')

    def test_func(self):
        artigo = self.get_object()
        return self.request.user == artigo.autor or self.request.user in artigo.colaboradores.all()

class FeedView(ListView):
    model = Artigo
    template_name = 'artigos/feed.html'
    context_object_name = 'artigos'
    ordering = ['-id'] 

class PedidoColaboracaoCreateView(LoginRequiredMixin, View):
    def post(self, request, artigo_id):
        artigo = get_object_or_404(Artigo, id=artigo_id)

        if artigo.autor == request.user:
            messages.error(request, "Você não pode solicitar colaboração no seu próprio artigo.")
            return redirect('detalhe_artigo', pk=artigo.id)

        pedido_existe = PedidoColaboracao.objects.filter(
            artigo=artigo, solicitante=request.user, status='pendente'
        ).exists()

        if pedido_existe:
            messages.warning(request, "Você já solicitou colaboração para este artigo e está pendente.")
        else:
            PedidoColaboracao.objects.create(
                artigo=artigo,
                solicitante=request.user,
                status='pendente'
            )
            messages.success(request, "Pedido de colaboração enviado com sucesso!")

        return redirect('detalhe_artigo', pk=artigo.id)
    
class PedidoColaboracaoListView(LoginRequiredMixin, ListView):
    model = PedidoColaboracao
    template_name = 'artigos/pedidos_colaboracao_recebidos.html'
    context_object_name = 'pedidos'

    def get_queryset(self):
        return PedidoColaboracao.objects.filter(
            artigo__autor=self.request.user,
            status='pendente'
        ).order_by('-created_at')
    
class PedidoColaboracaoDecidirView(LoginRequiredMixin, View):
    def post(self, request, pedido_id):
        pedido = get_object_or_404(PedidoColaboracao, id=pedido_id)

        if pedido.artigo.autor != request.user:
            messages.error(request, "Você não tem permissão para executar essa ação.")
            return redirect('profile')

        decisao = request.POST.get('decisao')
        if decisao == 'aceitar':
            pedido.status = 'aceito'
            pedido.artigo.colaboradores.add(pedido.solicitante)
            messages.success(request, f"Colaboração aceita para {pedido.solicitante.username}.")
        elif decisao == 'recusar':
            pedido.status = 'rejeitado'
            messages.info(request, f"Colaboração recusada para {pedido.solicitante.username}.")
        else:
            messages.error(request, "Decisão inválida.")
            return redirect('profile')  

        pedido.save()
        return redirect('profile')  
