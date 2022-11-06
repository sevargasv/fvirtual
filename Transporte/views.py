from django.shortcuts import render
from Transporte.models import Subasta, TransSubasta, Transporte, Vehiculo, Venta, DetalleVenta, Producto, Oferta, Solicitud, Cliente

# Create your views here.

def Transporte(request):
    return render(request, "Transporte/Transporte.html")