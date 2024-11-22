from django.urls import path
from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls  # Asegúrate de que esta variable esté bien nombrada
