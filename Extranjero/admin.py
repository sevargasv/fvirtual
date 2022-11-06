from django.contrib import admin
from Extranjero.models import Solicitud, DetalleSolicitud, Cliente

# Register your models here.

admin.site.register(Solicitud)
admin.site.register(DetalleSolicitud)
admin.site.register(Cliente)