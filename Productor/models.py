from django.db import models

# Create your models here.

class Productor(models.Model):
    productor_id = models.BigIntegerField(primary_key=True)
    estado = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=200)
    razon_social = models.CharField(max_length=100)
    rut_productor = models.BigIntegerField()
    dv_productor = models.CharField(max_length=5)
    fecha_alta = models.DateField()
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'productor'

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

class Producto(models.Model):
    producto_id = models.BigIntegerField(primary_key=True)
    producto = models.CharField(max_length=50)
    imagen_producto = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'

class Contrato(models.Model):
    contrato_id = models.BigIntegerField(primary_key=True)
    estado = models.CharField(max_length=10)
    rol_contrato = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha_ini = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    productor_productor = models.ForeignKey('Productor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contrato'

class ProductorOferta(models.Model):
    prod_ofer_id = models.BigIntegerField(primary_key=True)
    fecha_oferta = models.DateField()
    productor_productor = models.ForeignKey(Productor, models.DO_NOTHING)
    oferta_oferta = models.ForeignKey(Oferta, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'productor_oferta'

