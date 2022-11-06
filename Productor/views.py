from django.shortcuts import render
from Productor.models import Producto, Productor, ProductorOferta, Contrato, Oferta

# Create your views here.

def Productor(request):
    return render(request, "Productor/Productor.html")


def Productor1(request):

    ofertas=Oferta.objects.all()
    return render(request,"Productor/productor1.html", {"ofertas":ofertas})