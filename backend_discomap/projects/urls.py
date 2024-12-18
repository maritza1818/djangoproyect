from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import EventoViewSet, UserProfileViewSet  # Importar los nuevos viewsets
from .api import ProjectViewSet  # Asegurarnos de mantener esta importación
from . import views

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'perfiles', UserProfileViewSet)
router.register(r'api/tasks', ProjectViewSet, 'tasks')  # Mantener esta ruta

urlpatterns = [
    path('', views.helloworld, name='home'),
    path('signup/', views.helloworld),
    path('', include(router.urls)),  # Incluir las rutas del router
]


