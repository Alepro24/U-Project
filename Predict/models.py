from django.db import models
from AppLogin.models import Usuario
from App1.models import encuesta,poblacion

# Create your models here.
class modelousado(models.Model):
    id_Modelo = models.AutoField(primary_key=True)
    Tipo_modelo = models.CharField(max_length=20)
    Nombre_modelo = models.CharField(max_length=20)
    Estado =models.BooleanField()

class dato_entrenamiento(models.Model):
    id_Dato = models.AutoField(primary_key=True)
    Grupo_encuesta = models.ForeignKey(encuesta,on_delete=models.CASCADE)

class prediccion(models.Model):
    id_Prediccion = models.AutoField(primary_key=True)
    Nro_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    id_Modelo = models.ForeignKey(modelousado,on_delete=models.CASCADE)
    id_Dato = models.ForeignKey(dato_entrenamiento,on_delete=models.CASCADE)
    Fecha = models.DateField()

class dato_proyectado(models.Model):
    id_Datop = models.AutoField(primary_key=True)
    Año = models.IntegerField()
    id_Poblacion = models.ForeignKey(poblacion,on_delete=models.CASCADE)
    Demanda = models.IntegerField()
    id_Prediccion = models.ForeignKey(prediccion,on_delete=models.CASCADE)