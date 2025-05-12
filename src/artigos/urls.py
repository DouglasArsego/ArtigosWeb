from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtigoListView.as_view(), name='lista_artigos'),
    path('criar/', views.ArtigoCreateView.as_view(), name='criar_artigo'),
    path('<int:pk>/', views.ArtigoDetailView.as_view(), name='detalhe_artigo'),
    path('<int:pk>/editar/', views.ArtigoUpdateView.as_view(), name='editar_artigo'),
]
