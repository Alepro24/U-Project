from django.db import models

# Create your models here.

class Usuario(models.Model):
    Nro_Usuario = models.AutoField(primary_key=True)
    Usuario= models.CharField(max_length=30)
    Contrasena = models.CharField(max_length=30, verbose_name="Contraseña")
    Estado = models.BooleanField()

    def __str__(self):
        return self.Usuario
