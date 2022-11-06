from django.shortcuts import render
from Local.models import Cliente, Producto, Oferta

# Create your views here.

def Local(request):

    productos=Producto.objects.all()
    ofertas=Oferta.objects.all()
    if request.GET.get('calidad')!=None:
        calidadGet=request.GET["calidad"]
        return render(request,"Local/Local.html", {"productos":productos, "ofertas":ofertas, "calidadGet":calidadGet})
    else:
        return render(request,"Local/Local.html", {"productos":productos, "ofertas":ofertas})