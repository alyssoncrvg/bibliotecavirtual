from django.shortcuts import  redirect, render
from .forms import *
from django.contrib import messages
from .models import *
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse


def cadastro_livro(request, template_name='livro/cadastro_livro.html'):
    Livro = livros.objects.all()
    Genero = genero.objects.all()
    if request.method=='POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=LivroForm()
    return render(request, template_name, {'form':form,'Livro':Livro, 'Genero':Genero})

def cadastro_genero(request, template_name='genero/cadastro_genero.html'):
    Genero = genero.objects.all()
    if request.method=='POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
                form.save()
                messages.success(request, 'Gênero Cadastrado com sucesso')
        return redirect('cadastro_genero')

    else:
        form=GeneroForm()
    return render(request, template_name, {'form':form, 'Genero':Genero})

def editar_livro(request,id, template_name='livro/editar_livro.html'):
    Livro = livros.objects.get(id=id)
    form = LivroForm(request.POST, request.FILES, instance=Livro)
    if form.is_valid():
        form.save()
        return redirect('detail_livros', id=Livro.id)
    else:
        form = LivroForm(instance=Livro)
    return render(request, template_name, {'form':form, 'Livro':Livro})

def editar_genero(request, id, template_name='editar_genero.html'):
    Genero = genero.objects.get(id=id)
    form = GeneroForm(request.POST, instance=genero)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        form = GeneroForm(instance=genero)
    return render(request, template_name, {'Genero': Genero, 'form':form})

# def deletar_livro(request, id):
#     Livro = livros.objects.get(id=id)
#     Livro.delete()
#     return HttpResponse('')

def deletar_livro(request, id, template_name='livro/deletar_livro.html'):
    Livro = livros.objects.get(id=id)

    if request.method== 'POST':
        Livro.delete()
        return HttpResponseRedirect('/')
    
    return render(request, template_name, {'livro':Livro})


def deletar_genero(request, id):
    Genero = genero.objects.get(id=id)
    Genero.delete()
    return HttpResponse('')

def listar_livro(request, template_name='livro/lista.html'):
    query = request.GET.get("buscar_livro")
    if query:
        Livro = livros.objects.filter(titulo__icontains=query)
    else:
        Livro = livros.objects.all()
    list_livro = {'list_livro': Livro}
    return render(request, template_name, list_livro)

def detail_livro(request, id):
    Livro = livros.objects.get(id=id)

    return render(request, 'livro/detail_livro.html', {'livro':Livro})