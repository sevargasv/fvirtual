from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, "FeriaVirtual/home.html")

def nosotros(request):
    return render(request, "FeriaVirtual/nosotros.html")

def contacto(request):
    return render(request, "FeriaVirtual/contacto.html")

def registro(request):

    if request.method=="POST":
        
        subject=request.POST["nombre"]+request.POST["paterno"]
        message=request.POST["rsocial"]+"\n"+request.POST["mail"]+"\n"+request.POST["rut"]+"-"+request.POST["dvrut"]+"\n"+request.POST["pais"]+"\n"+request.POST["rol"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["empresa.maipogrande@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
    
    return render(request,"FeriaVirtual/registro.html")
    