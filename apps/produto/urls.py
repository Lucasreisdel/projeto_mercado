from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página inicial
    path('loja/', views.index_loja, name='index_loja'),
    path('estoque/', views.index_estoque, name='index_estoque'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('editar/<int:produto_id>/', views.editar, name='editar'),
    path('excluir/<int:produto_id>/', views.excluir, name='excluir'),
]
