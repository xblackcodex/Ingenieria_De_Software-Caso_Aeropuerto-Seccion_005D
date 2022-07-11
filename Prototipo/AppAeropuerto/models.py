from django.db import models

# Create your models here.

class Categoria (models.Model): 
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoría')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre de Categoría')

    def __str__(self):
        return self.nombreCategoria

class Vehiculo(models.Model):
    patente = models.CharField(max_length=9, primary_key=True, verbose_name='Patente')
    chofer = models.CharField(max_length=20, verbose_name='Chofer')
    modelo = models.CharField(max_length=30, verbose_name='Modelo')
    ubicacionsal = models.CharField(max_length=40, verbose_name='Ubicacion_Salida')
    cantdisponible = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente
