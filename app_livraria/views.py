from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Autor, Categoria

def home(request):
    return render(request, 'pages/home.html')

# CREATE
def criarAutor(request):
    if request.method == "POST":
        novo_autor = Autor()
        novo_autor.nome = request.POST.get('nomeAutor')
        novo_autor.data_nascimento = request.POST.get('dataNascimento')
        novo_autor.pais_origem = request.POST.get('paisOrigem')
        novo_autor.save()
        
        return redirect('home')  

    return render(request, 'pages/criarAutor.html')

def criarCategoria(request):
    if request.method == "POST":
        nova_categoria = Categoria()
        nova_categoria.nome = request.POST.get('categoriaBook')
        nova_categoria.save()
        return redirect('home')

    return render(request, 'pages/criarCategoria.html')

def criarLivros(request):
    if request.method == "POST":
        novo_livro = Livro()
        novo_livro.titulo = request.POST.get('nameBook')
        novo_livro.autor_id = request.POST.get('autorBook') 
        novo_livro.categoria_id = request.POST.get('categoriaBook') 
        novo_livro.ano_publicacao = request.POST.get('yearBook')
        novo_livro.isbn = request.POST.get('isbnBook')
        novo_livro.save()
        return redirect('home') 

    autores = Autor.objects.all()
    categorias = Categoria.objects.all()

    context = {
        'autores': autores,
        'categorias': categorias,
    }

    return render(request, 'pages/criarLivros.html', context)

# GET
def listarAutor(request):
    autores = Autor.objects.all()
    return render(request, 'pages/listarAutor.html', {'autores': autores})

def listarCategoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'pages/listarCategoria.html', {'categorias': categorias})

def listarLivros(request):
    livros = Livro.objects.all()
    return render(request, 'pages/livros.html', {'livros': livros})

# DELETE 
def excluirAutor(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.delete()
    return redirect('listar_autor') 

def excluirCategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('listar_categoria') 

def excluirLivro(request, id):
    livro = get_object_or_404(Livro, id=id)
    livro.delete()
    return redirect('listar_livros')

# UPDATE
def editarAutor(request, id):
    autor = get_object_or_404(Autor, id=id)

    if request.method == "POST":
        autor.nome = request.POST.get('nomeAutor')
        autor.data_nascimento = request.POST.get('dataNascimento')
        autor.pais_origem = request.POST.get('paisOrigem')
        autor.save()  
        return redirect('listar_autor')

    return render(request, 'pages/editarAutor.html', {'autor': autor})

def editarCategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == "POST":
        categoria.nome = request.POST.get('categoriaBook')
        categoria.save()  
        return redirect('listar_categoria')

    return render(request, 'pages/editarCategoria.html', {'categoria': categoria})

def editarLivro(request, id):
    livro = get_object_or_404(Livro, id=id)
    categorias = Categoria.objects.all()
    autores = Autor.objects.all()

    if request.method == "POST":
        livro.titulo = request.POST.get('nameBook')
        livro.autor_id = request.POST.get('autorBook') 
        livro.categoria_id = request.POST.get('categoriaBook') 
        livro.ano_publicacao = request.POST.get('yearBook')
        livro.isbn = request.POST.get('isbnBook')
        livro.save()
        return redirect('listar_livros')

    return render(request, 'pages/editarLivro.html', {'livro': livro, 'categorias': categorias, 'autores': autores})
