from django.db import models

# Create your models here.

class Transporte(models.Model):
    empresa_id = models.BigIntegerField(primary_key=True)
    estado = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=200)
    razon_social = models.CharField(max_length=200)
    rut_transporte = models.BigIntegerField()
    dv_transporte = models.CharField(max_length=2)
    fecha_alta = models.DateField()
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'transporte'

class Vehiculo(models.Model):
    transporte_id = models.BigIntegerField(primary_key=True)
    estado = models.CharField(max_length=10)
    patente = models.CharField(max_length=20)
    tipo_vehiculo = models.CharField(max_length=50)
    carga_util = models.CharField(max_length=20)
    transporte_empresa = models.ForeignKey(Transporte, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vehiculo'

class TransSubasta(models.Model):
    proceso_id = models.BigIntegerField(primary_key=True)
    estado = models.CharField(max_length=10)
    fecha_oferta = models.DateField()
    precio_ofertado = models.FloatField()
    transporte_empresa = models.ForeignKey('Transporte', models.DO_NOTHING)
    subasta_subasta = models.ForeignKey('Subasta', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'trans_subasta'

class Subasta(models.Model):
    subasta_id = models.BigIntegerField(primary_key=True)
    estado = models.CharField(max_length=1)
    precio = models.FloatField()
    venta_venta_field = models.ForeignKey('Venta', models.DO_NOTHING, db_column='venta_venta__id')  # Field renamed because it ended with '_'.
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    tipo_vehiculo = models.CharField(max_length=100)
    peso_carga = models.FloatField()
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subasta'

class Venta(models.Model):
    venta_id = models.BigIntegerField(db_column='venta__id', primary_key=True)  # Field renamed because it contained more than one '_' in a row.
    estado = models.CharField(max_length=10)
    tipo_venta = models.CharField(max_length=50)
    total = models.FloatField()
    fecha_venta = models.DateField()
    impuestos = models.FloatField()
    solicitud_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'venta'

class DetalleVenta(models.Model):
    detalle_venta_id = models.BigIntegerField(primary_key=True)
    cantidad = models.FloatField()
    precio_bruto = models.FloatField()
    uni_medida = models.CharField(max_length=10)
    venta_venta_field = models.ForeignKey('Venta', models.DO_NOTHING, db_column='venta_venta__id')  # Field renamed because it ended with '_'.
    oferta_oferta = models.ForeignKey('Oferta', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'detalle_venta'

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