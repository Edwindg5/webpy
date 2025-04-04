from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
