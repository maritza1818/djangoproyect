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


