from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(' ',views.Productor, name="Productor"),
    path('pro1/',views.Productor1, name="Productor1"),
]