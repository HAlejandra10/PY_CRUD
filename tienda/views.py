from django.shortcuts import render

# Create your views here.
def hola(request):
    return render(request, "plantilla.html")

#render(request,"prueba.html") 