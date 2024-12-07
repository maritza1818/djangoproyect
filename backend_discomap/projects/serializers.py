from rest_framework import serializers
from .models import Project, Discoteca
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class DiscotecaSerializer(serializers.ModelSerializer):
    user = UserSerializer()  

    class Meta:
        model = Discoteca
        fields = ['id', 'nombre', 'direccion', 'horario_apertura', 'horario_cierre', 
                  'aforo_maximo', 'stock_bebidas', 'calificacion', 'descripcion', 
                  'created_at', 'user']

class ProjectSerializer(serializers.ModelSerializer):
    discoteca = DiscotecaSerializer() 
    user = UserSerializer()  

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'datecompleted', 
                  'created_at', 'discoteca', 'user', 'important']
        read_only_fields = ('created_at',)
