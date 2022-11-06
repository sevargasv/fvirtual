from django.contrib import admin
from Local.models import Cliente, Oferta, Producto

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Oferta)
admin.site.register(Producto)