from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, CustomRegisterView, UserProfileView, PublicUserProfileView, EditarPerfilView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/editar/', EditarPerfilView.as_view(), name='editar_perfil'),
    path('usuario/<slug:username>/', PublicUserProfileView.as_view(), name='perfil_publico'),
]
