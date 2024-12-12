from rest_framework import viewsets
from .models import Project, Discoteca
from django.contrib.auth.models import User
from .serializers import UserSerializer, DiscotecaSerializer, ProjectSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar operaciones CRUD de usuarios
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DiscotecaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar operaciones CRUD de discotecas
    """
    queryset = Discoteca.objects.all()
    serializer_class = DiscotecaSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar operaciones CRUD de proyectos asociados a discotecas
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer