from rest_framework import serializers
from .models import Project, Discoteca, Reserva, Comentario, Evento, Favorito
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password1', 'password2']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user

class DiscotecaSerializer(serializers.ModelSerializer):
    user = UserSerializer()  

    class Meta:
        model = Discoteca
        fields = ['promociones','id', 'nombre', 'direccion', 'horario_apertura', 'horario_cierre', 
                  'aforo_maximo', 'stock_bebidas', 'calificacion', 'descripcion', 
                  'created_at', 'user', 'imagen', 'telefono', 'redes_sociales', 
                  'precio_entrada', 'latitud', 'longitud', 'servicios', 'estado_abierta'
                  ]

class ProjectSerializer(serializers.ModelSerializer):
    discoteca = DiscotecaSerializer() 
    user = UserSerializer()  

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'datecompleted', 
                  'created_at', 'discoteca', 'user', 'important']
        read_only_fields = ('created_at',)

class ReservaSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    discoteca = DiscotecaSerializer()

    class Meta:
        model = Reserva
        fields = ['id', 'user', 'discoteca', 'fecha', 'hora', 'cantidad_personas', 'created_at']
        read_only_fields = ('created_at',)

class ComentarioSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    discoteca = DiscotecaSerializer()

    class Meta:
        model = Comentario
        fields = ['id', 'user', 'discoteca', 'texto', 'calificacion', 'created_at']
        read_only_fields = ('created_at',)

class EventoSerializer(serializers.ModelSerializer):
    discoteca = DiscotecaSerializer()

    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'descripcion', 'fecha', 'hora_inicio', 'hora_fin', 'discoteca', 'created_at']
        read_only_fields = ('created_at',)

class FavoritoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    discoteca = DiscotecaSerializer()

    class Meta:
        model = Favorito
        fields = ['id', 'user', 'discoteca', 'created_at']
        read_only_fields = ('created_at',)
