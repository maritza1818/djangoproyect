from .models import Project, Discoteca
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer, DiscotecaSerializer
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

class DiscotecaViewSet(viewsets.ModelViewSet):
    queryset = Discoteca.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = DiscotecaSerializer