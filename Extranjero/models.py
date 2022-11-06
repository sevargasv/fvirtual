from django.db import models

# Create your models here.
class DetalleSolicitud(models.Model):
    detalle_id = models.BigIntegerField(primary_key=True)
    producto = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=20)
    solicitud_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING)
    cantidad = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_solicitud'

class Solicitud(models.Model):
    solicitud_id = models.BigIntegerField(primary_key=True)
    estado = models.CharField(max_length=10)
    fecha_solicitud = models.DateField()
    cliente_cliente = models.ForeignKey('Cliente', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'solicitud'

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
