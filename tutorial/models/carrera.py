#tutorial/models/carrera.py
from django.db import models 


class Carrera(models.Model):
    
    nombre = models.CharField(max_length=50)
    descripcion= models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.nombre