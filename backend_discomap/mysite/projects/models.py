from django.db import models
from django.contrib.auth.models import User

# Modelo para representar una Discoteca
class Discoteca(models.Model):
    nombre = models.CharField(max_length=200)  # Nombre de la discoteca
    direccion = models.CharField(max_length=300)  # Dirección de la discoteca
    telefono = models.CharField(max_length=15, null=True, blank=True)  # Teléfono de contacto (opcional)
    horario_apertura = models.TimeField()  # Hora de apertura
    horario_cierre = models.TimeField()  # Hora de cierre
    stock_bebidas = models.IntegerField()  # Cantidad de bebidas disponibles
    aforo_maximo = models.IntegerField()  # Aforo máximo de la discoteca
    calificacion = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Calificación promedio
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario que registró la discoteca
    creado_en = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        return self.nombre

# Modelo para los Proyectos, como el que mencionaste
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discoteca = models.ForeignKey(Discoteca, on_delete=models.CASCADE)  # Relación con Discoteca

    def __str__(self):
        return self.title
