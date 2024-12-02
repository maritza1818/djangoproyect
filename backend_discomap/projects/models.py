from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#########################

class Discoteca(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    aforo_maximo = models.IntegerField()
    stock_bebidas = models.TextField()  # Detalle de bebidas disponibles
    calificacion = models.DecimalField(max_digits=3, decimal_places=2)  # Ej: 4.75
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    disco = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
