from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Artigo
from .forms import ArtigoForm

class ArtigoListView(LoginRequiredMixin, ListView):
    model = Artigo
    template_name = 'artigos/lista_artigos.html'
    context_object_name = 'artigos'

class ArtigoDetailView(LoginRequiredMixin, DetailView):
    model = Artigo
    template_name = 'artigos/detalhe_artigo.html'

class ArtigoCreateView(LoginRequiredMixin, CreateView):
    model = Artigo
    form_class = ArtigoForm   # <-- aqui
    template_name = 'artigos/form_artigo.html'
    success_url = reverse_lazy('lista_artigos')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ArtigoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Artigo
    form_class = ArtigoForm   # <-- e aqui
    template_name = 'artigos/form_artigo.html'
    success_url = reverse_lazy('lista_artigos')

    def test_func(self):
        artigo = self.get_object()
        return self.request.user == artigo.autor or self.request.user in artigo.colaboradores.all()