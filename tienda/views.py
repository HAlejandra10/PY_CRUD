from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "main.html")

#render(request,"prueba.html")

def consulproducts(request):
    return render(request, "products.html")