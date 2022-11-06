from django.shortcuts import render
from Extranjero.models import Solicitud, DetalleSolicitud, Cliente
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def Extranjero(request):

    if request.method=="POST":
        
        subject=request.POST["nombre"]
        message=request.POST["rut"]+"\n"+request.POST["producto"]+"\n"+request.POST["cantidad"]+"-"+request.POST["medida"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["empresa.maipogrande@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
    
    return render(request, "Extranjero/Extranjero.html")