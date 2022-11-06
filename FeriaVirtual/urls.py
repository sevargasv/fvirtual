from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name="Home"),
    path('nosotros/',views.nosotros, name="Nosotros"),
    path('contacto/',views.contacto, name="Contacto"),
    path('registro/',views.registro, name="Registro"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)