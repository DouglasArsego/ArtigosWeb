from django.urls import path
from .views import CustomLoginView, CustomRegisterView, UserProfileView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
