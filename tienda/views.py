from django.shortcuts import render
from tienda.models import Productos

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
    nombre= request.POST["nombre"]
    precio= request.POST["precio"]
    descripcion= request.POST["description"]
    