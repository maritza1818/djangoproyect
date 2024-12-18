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


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiscotecaViewSet_DRF, ProjectViewSet_DRF, ReservaViewSet_DRF, ComentarioViewSet_DRF, EventoViewSet_DRF, FavoritoViewSet_DRF

router = DefaultRouter()
router.register(r'discotecas-drf', DiscotecaViewSet_DRF)
router.register(r'projects-drf', ProjectViewSet_DRF)
router.register(r'reservas-drf', ReservaViewSet_DRF)
router.register(r'comentarios-drf', ComentarioViewSet_DRF)
router.register(r'eventos-drf', EventoViewSet_DRF)
router.register(r'favoritos-drf', FavoritoViewSet_DRF)

urlpatterns = [
    path('api/', include(router.urls)),
]


