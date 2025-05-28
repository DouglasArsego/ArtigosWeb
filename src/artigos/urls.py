from django.urls import path
from . import views

urlpatterns = [
    path('', views.FeedView.as_view(), name='lista_artigos'),
    path('criar/', views.ArtigoCreateView.as_view(), name='criar_artigo'),
    path('<int:pk>/', views.ArtigoDetailView.as_view(), name='detalhe_artigo'),
    path('<int:pk>/editar/', views.ArtigoUpdateView.as_view(), name='editar_artigo'),

    path('pedido-colaboracao/criar/<int:artigo_id>/', views.PedidoColaboracaoCreateView.as_view(), name='pedido_colaboracao_criar'),
    path('pedidos-colaboracao/', views.PedidoColaboracaoListView.as_view(), name='pedidos_colaboracao_recebidos'),
    path('pedido-colaboracao/decidir/<int:pedido_id>/', views.PedidoColaboracaoDecidirView.as_view(), name='pedido_colaboracao_decidir'),

    path('dicas/', views.dicas_view, name='dicas'),
    path('noticias/', views.noticias_view, name='noticias'),
]

