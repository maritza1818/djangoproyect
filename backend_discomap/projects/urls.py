from django.urls import path
from rest_framework import routers
from .api import ProjectViewSet

from . import views

urlpatterns = [
    path('', views.helloworld, name='home'),  
    path('signup/', views.helloworld)
]

router = routers.DefaultRouter()
router.register('api/tasks', ProjectViewSet, 'tasks')

urlpatterns = router.urls  
