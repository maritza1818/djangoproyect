from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from projects import views
from projects.api import ProjectViewSet, DiscotecaViewSet
from projects.viewsets import EventoViewSet, UserProfileViewSet  # Importar los nuevos viewsets
from django.conf import settings
from django.conf.urls.static import static
from projects.views import discotecas_json, tasks_json, signin, signup, signout
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'discotecas', DiscotecaViewSet, basename='discotecas')
router.register(r'eventos', EventoViewSet, basename='eventos')  # Registrar EventoViewSet
router.register(r'perfiles', UserProfileViewSet, basename='perfiles')  # Registrar UserProfileViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create', views.create_task, name='create_task'),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('discotecas/', views.discotecas, name='discotecas'),
    path('discotecas/create', views.create_discoteca, name='create_discoteca'),
    path('discotecas/<int:discoteca_id>', views.discoteca_detail, name='discoteca_detail'),
    path('discotecas/<int:discoteca_id>/complete', views.complete_discoteca, name='complete_discoteca'),
    path('discotecas/<int:discoteca_id>/like/', views.like_discoteca, name='like_discoteca'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('api/tasks/', views.tasks_json, name='tasks_json'),
    path('api/usuarios/login/', views.signin, name='login'),
    path('api/usuarios/register/', views.signup, name='register'),
    path('api/usuarios/logout/', views.signout, name='logout'),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

