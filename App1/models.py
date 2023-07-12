from django.db import models
from AppLogin.models import Usuario

# Create your models here.
class encuestaprueba(models.Model):
    Paterno= models.CharField(max_length=30)
    Materno = models.CharField(max_length=30)
    Nombre = models.CharField(max_length=30)
    Edad = models.IntegerField()

    def __str__(self):
        return self.Usuario

class encuesta(models.Model):
    Edad= models.IntegerField()
    Sexo= models.CharField(max_length=6)
    Zona= models.CharField(max_length=50)
    Vegano= models.CharField(max_length=2)
    Conocimiento_cereales_a= models.CharField(max_length=2)
    Consumio_cereales_e= models.CharField(max_length=2)
    Frecuencia_compra= models.CharField(max_length=50)
    Momento_consumo= models.CharField(max_length=50)
    Marca_cereal_consumo= models.CharField(max_length=30)
    Consumio_cereales_a= models.CharField(max_length=2)
    Cereal_a_consumido= models.CharField(max_length=50)
    Forma_consumo= models.CharField(max_length=50)
    Interes_aspectos_nutri= models.CharField(max_length=2)
    Influencia_compra= models.CharField(max_length=50)
    Precio_cantidad_apagar= models.CharField(max_length=50)
    Contenido= models.CharField(max_length=20)
    Sabor= models.CharField(max_length=30)

class productos(models.Model):
    id_Producto = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=20)
    Descripcion = models.CharField(max_length=25)
    Nro_Usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    Estado = models.BooleanField()

class poblacion(models.Model):
    id_Poblacion = models.AutoField(primary_key=True)
    Localidad = models.CharField(max_length=30)
    Anno = models.CharField(max_length=4,verbose_name="Año")
    Pet= models.IntegerField()
    Pea = models.IntegerField()
    Poblacion_segmentada = models.IntegerField()
    Mercado_potencial = models.IntegerField()
    Mercado_objetivo = models.IntegerField()
    Estado = models.BooleanField()

class cereal(models.Model):
    id_Cereal = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=25)
    Clase = models.CharField(max_length=25)
    Nro_Usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    Estado = models.BooleanField()

class dgeneral(models.Model):
    id_Cereal = models.IntegerField()
    Anno = models.CharField(max_length=4,verbose_name="Año")
    Lugar = models.CharField(max_length=25)
    Superficie = models.FloatField()
    Produccion = models.FloatField()
    Rendimiento = models.FloatField()
    Cant_exportacion= models.FloatField()

class cantcultivada(models.Model):
    id_Provincia = models.IntegerField()
    Provincia = models.CharField(max_length=30)
    Quinua = models.FloatField()
    Cebada = models.FloatField()
    Canahua = models.FloatField(verbose_name="Cañahua")


