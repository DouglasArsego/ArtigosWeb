from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, CustomRegisterView, UserProfileView, PublicUserProfileView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('usuario/<slug:username>/', PublicUserProfileView.as_view(), name='perfil_publico'),
]
