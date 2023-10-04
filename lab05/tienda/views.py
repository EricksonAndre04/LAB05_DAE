from django.shortcuts import render
from .models import Cliente 
from .models import Categoria, Producto
# Create your views here.
def index(request):
    return render(request, 'tienda/clientes.html')  

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'tienda/clientes.html', {'clientes': clientes})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'tienda/categorias.html', {'categorias': categorias})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/productos.html', {'productos': productos})
