from email.policy import default
from tkinter import CASCADE
from django.db import models

# Create your models here.

class genero(models.Model):
    genero = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.genero

class livros(models.Model):
    isbn = models.CharField(max_length=13, unique=True, null=False)
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    autor = models.CharField(max_length=200)
    genero = models.ManyToManyField(genero)
    foto = models.ImageField(upload_to='images', null=False)

    def __str__(self):
        return self.titulo