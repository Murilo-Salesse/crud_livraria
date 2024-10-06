from django.urls import path
from app_livraria import views

urlpatterns = [
    path('', views.home,name="home"),

    path('criar_autor/', views.criarAutor, name="criar_autor"),
    path('listar_autor/', views.listarAutor, name="listar_autor"),
    path('deletar_autor/<int:id>/', views.excluirAutor, name='excluir_autor'),
    path('editar_autor/<int:id>/', views.editarAutor, name='editar_autor'),

    path('criar_categoria/', views.criarCategoria, name="criar_categoria"),
    path('listar_categoria/', views.listarCategoria, name="listar_categoria"),
    path('deletar_categoria/<int:id>/', views.excluirCategoria, name="excluir_categoria"),
    path('editar_categoria/<int:id>/', views.editarCategoria, name='editar_categoria'),
    
    path('criar_livros/', views.criarLivros, name="criar_livro"),
    path('listar_livros/', views.listarLivros, name="listar_livros"),
    path('deletar_livro/<int:id>/', views.excluirLivro, name="excluir_livro"),
    path('editar_livro/<int:id>/', views.editarLivro, name='editar_livro'),
]
