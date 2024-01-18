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

def eliminar(request, id): 
    #pass
    producto = Productos.objects.filter(pk=id)
    producto.delete()
    messages.success(request, 'Producto Eliminado')
    return redirect('consultar')    
 
def detalle(request, id): 
    #pass
    producto = Productos.objects.get(pk=id)
    return render(request,"productoEditar.html", {
        'producto': producto
    })  
    
def editar(request): 
    n= request.POST["nombre"] 
    price= request.POST["precio"]
    descrip= request.POST["description"]
    id= request.POST["id"]
    Productos.objects.filter(pk=id).update(id=id, nombre=n, precio=price, description=descrip)
    messages.success(request, 'Producto Actualizado')
    return redirect('consultar')