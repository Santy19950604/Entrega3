from django.shortcuts import render
from .models import Autor, Categoria, Post
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaForm

def home(request):
    return render(request, 'blog/home.html')

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AutorForm()
    return render(request, 'blog/formulario.html', {'form': form, 'tipo': 'Autor'})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriaForm()
    return render(request, 'blog/formulario.html', {'form': form, 'tipo': 'Categoría'})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'blog/formulario.html', {'form': form, 'tipo': 'Post'})

def buscar_post(request):
    resultado = []
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultado = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaForm()
    return render(request, 'blog/buscar.html', {'form': form, 'resultado': resultado})
