from django.db import models


# Create your models here.

class Cliente(models.Model):
    cliente_id = models.BigIntegerField(primary_key=True)
    estado = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=200)
    rut_cliente = models.IntegerField()
    dv_cliente = models.CharField(max_length=5)
    fecha_alta = models.DateField()
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    ap_paterno = models.CharField(max_length=50, blank=True, null=True)
    ap_materno = models.CharField(max_length=50, blank=True, null=True)
    codigo_postal = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    pais = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name="Cliente"
        verbose_name_plural="Clientes"


class Oferta(models.Model):
    oferta_id = models.BigIntegerField(primary_key=True)
    estado = models.CharField(max_length=10)
    uni_medida = models.CharField(max_length=20)
    cantidad = models.FloatField()
    precio = models.FloatField()
    calidad = models.CharField(max_length=15)
    producto_producto = models.ForeignKey('Producto', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oferta'
        verbose_name="Oferta"
        verbose_name_plural="Ofertas"
        

class Producto(models.Model):
    producto_id = models.BigIntegerField(primary_key=True)
    producto = models.CharField(max_length=50)
    imagen_producto = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'
        verbose_name="Producto"
        verbose_name_plural="Productos"
    
