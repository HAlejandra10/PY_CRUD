from django.shortcuts import render, redirect
from tienda.models import Productos
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "main.html")

#render(request,"prueba.html")

def consulproducts(request):
    productos= Productos.objects.all()
    return render(request, "productos.html", {
        'productos': productos
    })
    
def guardar(request):
    n= request.POST["nombre"]
    price= request.POST["precio"]
    descrip= request.POST["description"]
    p = Productos(nombre= n, precio=price, description=descrip) #crear product ,el nombre= es el mismo nombre que está en models.py
    p.save()
    messages.success(request, 'Producto Agregado')
    return redirect('consultar')
    
    