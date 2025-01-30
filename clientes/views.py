from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Clientes

def listar_clientes(request):
    clientes = Clientes.objects.all()
    context = {
        "clientes" : clientes,
    }
    return render(request, 'clientes/listar.html', context=context)

def agregar_cliente(request):
    return render(request, 'clientes/crear.html')


def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']
        
        cliente = Clientes.objects.create(nombre=nombre, email=email, telefono=telefono)
        cliente.save()
    return redirect('listar_clientes')


def actualizar_cliente(request, id):
    cliente = Clientes.objects.get(id=id)
    context = {
        "cliente" : cliente,
    }
    return render(request, "clientes/actualizar.html", context)



def actualizar(request, id): 
    cliente = Clientes.objects.get(id=id) 
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']
        
    cliente.nombre = nombre
    cliente.email = email
    cliente.telefono = telefono
    cliente.save()

    return redirect('listar_clientes')



def eliminar_cliente(request, id):
    cliente = Clientes.objects.get(id=id)
    cliente.delete()
    return redirect('listar_clientes')

# Create your views here.
