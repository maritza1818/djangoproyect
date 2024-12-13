from rest_framework import viewsets, permissions
from .models import Project, Discoteca
from django.contrib.auth.models import User
from .serializers import UserSerializer, DiscotecaSerializer, ProjectSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class DiscotecaViewSet(viewsets.ModelViewSet):
    user = UserSerializer()
    queryset = Discoteca.objects.all()
    serializer_class = DiscotecaSerializer
    permission_classes = [permissions.AllowAny]


class ProjectViewSet(viewsets.ModelViewSet):
    discoteca = DiscotecaSerializer()  # Relación anidada
    user = UserSerializer()
    permission_classes = [permissions.AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
