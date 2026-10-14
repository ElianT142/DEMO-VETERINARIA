from django.db import models

# Create your models here.

class cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    

    def __str__(self):
        return self.nombre


class atencion(models.Model):
    nombre = models.CharField(max_length=100)
    cliente = models.ForeignKey(cliente, on_delete=models.PROTECT,related_name= 'atenciones')
    tipo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)