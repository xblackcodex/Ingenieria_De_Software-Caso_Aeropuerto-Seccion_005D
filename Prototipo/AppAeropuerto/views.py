from django.shortcuts import render, redirect
from django.views.decorators import csrf
from .models import Vehiculo
from .forms import VehiculoForm

def inicio(request):
    return render (request, 'inicio.html')

def mostrar(request):
    return render (request, 'mostrar.html')

def mostrar(request):
    vehiculos = Vehiculo.objects.all()
    datos = {
        'vehiculos' : vehiculos
    }
    return render(request,'mostrar.html',datos)