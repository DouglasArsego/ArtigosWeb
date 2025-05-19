
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from artigos.models import Artigo
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth import get_user_model

def home(request):
    return render(request, 'home.html')

# View para Login
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

# View para Registro
class CustomRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

# View para o Perfil do Usuário
class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['meus_artigos'] = Artigo.objects.filter(autor=user).order_by('-id')
        context['colaboracoes'] = Artigo.objects.filter(colaboradores=user).exclude(autor=user).order_by('-id')
        return context
