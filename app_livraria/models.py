from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    pais_origem = models.CharField(max_length=50)

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

class Livro(models.Model):
    titulo = models.CharField(max_length=200, null=True, blank=True)  
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True, blank=True)  
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)  
    ano_publicacao = models.DateField(null=True, blank=True)  
    isbn = models.CharField(max_length=13, null=True, blank=True)  
