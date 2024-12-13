from rest_framework import viewsets
from .models import Project, Discoteca
from django.contrib.auth.models import User
from .serializers import UserSerializer, DiscotecaSerializer, ProjectSerializer

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class DiscotecaViewSet(viewsets.ModelViewSet):
 
    queryset = Discoteca.objects.all()
    serializer_class = DiscotecaSerializer

class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer