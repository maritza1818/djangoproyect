from django.db import models
from django.contrib.auth.models import User


class Discoteca(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    aforo_maximo = models.IntegerField()
    stock_bebidas = models.TextField()
    calificacion = models.DecimalField(
        max_digits=3, decimal_places=2)  # Ej: 4.75
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    imagen = models.URLField(null=True, blank=True)
    telefono = models.CharField(
        max_length=15, null=True, blank=True)  
    redes_sociales = models.JSONField(blank=True, null=True)
    precio_entrada = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True) 
    latitud = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True) 
    longitud = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    servicios = models.TextField(
        blank=True, null=True) 
    estado_abierta = models.BooleanField(
        default=True)
    promociones = models.TextField(
        blank=True, null=True) 
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='discotecas')

    def promedio_calificaciones(self):
        comentarios = self.comentarios.all()
        total = sum([comentario.calificacion for comentario in comentarios])
        return total / comentarios.count() if comentarios.count() > 0 else 0.0

    def __str__(self):
        return self.nombre


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    discoteca = models.ForeignKey(
        Discoteca, on_delete=models.CASCADE, related_name='projects')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '- by' + self.user.username


class Reserva(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reservas')
    discoteca = models.ForeignKey(
        Discoteca, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reserva de {self.user.username} en {self.discoteca.nombre}'


class Comentario(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comentarios')
    discoteca = models.ForeignKey(
        Discoteca, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    calificacion = models.DecimalField(
        max_digits=3, decimal_places=2)  # Ej: 4.5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.calificacion}⭐'


class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    discoteca = models.ForeignKey(
        Discoteca, on_delete=models.CASCADE, related_name='eventos')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Evento: {self.nombre} en {self.discoteca.nombre}'


class Favorito(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favoritos')
    discoteca = models.ForeignKey(
        Discoteca, on_delete=models.CASCADE, related_name='favoritos')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'discoteca')  

    def __str__(self):
        return f'{self.user.username} añadió {self.discoteca.nombre} a favoritos'
