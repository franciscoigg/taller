from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request,'app1/inicio.html')

def tatuadores(request):
    return render(request,'app1/tatuadores.html')

def galeria(request):
    return render(request,'app1/galeria.html')

def contacto(request):
    return render(request,'app1/contacto.html')