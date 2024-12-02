from rest_framework import serializers
from .models import Project, Discoteca
from django.contrib.auth.models import User

class DiscotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discoteca
        fields = ['id', 'nombre', 'direccion', 'horario_apertura', 'horario_cierre', 'aforo_maximo', 'stock_bebidas', 'calificacion', 'descripcion', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Puedes añadir más campos si lo deseas

class ProjectSerializer(serializers.ModelSerializer):
    disco = DiscotecaSerializer()  # Utiliza un serializer anidado para la relación con Discoteca
    user = UserSerializer()  # Utiliza un serializer anidado para la relación con el usuario

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'datecompleted', 'created_at', 'disco', 'user', 'important']
        read_only_fields = ('created_at',)  # Es correcto que 'created_at' sea solo de lectura
