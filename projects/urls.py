from django.urls import path
from rest_framework import routers
from .api import ProjectViewSet

from . import views

urlpatterns = [
    path('', views.helloworld, name='home'),  # Página principal dentro del proyecto
    # Otras rutas específicas del proyecto
]

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls  # Asegúrate de que esta variable esté bien nombrada
