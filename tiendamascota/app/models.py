from distutils.command.upload import upload
from django.db import models
from django.utils import timezone

class Mascota(models.Model):
    raza=models.CharField(max_length=20)
    peso=models.IntegerField()
    estatura=models.IntegerField()
    annos_de_vida=models.IntegerField()
    precio=models.IntegerField()
    
    def __str__(self):
        return self.raza

class Producto(models.Model):
    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    precio=models.IntegerField()
    
    def __str__(self):
        return self.codigo
    

opciones_consultas = [
    [0,"consulta"],
    [1,"reclamo"], 
    [2,"sugerencia"],
    [3,"agradecimientos"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre