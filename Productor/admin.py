from django.contrib import admin
from Productor.models import Productor, Oferta, Producto, Contrato, ProductorOferta

# Register your models here.

admin.site.register(Producto)
admin.site.register(Oferta)
admin.site.register(ProductorOferta)
admin.site.register(Productor)
admin.site.register(Contrato)
