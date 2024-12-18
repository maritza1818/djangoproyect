"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from projects import views


urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta del panel de administración
    path('', views.home, name='home'),  # Página principal dentro del proyecto
    # Otras rutas específicas del proyecto
    # Página principal con "Hello world!!!"
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create', views.create_task, name='create_task'),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('discotecas/', views.discotecas, name='discotecas'),
    path('discotecas/create', views.create_discoteca, name='create_discoteca'),
    path('discotecas/<int:discoteca_id>', views.discoteca_detail, name='discoteca_detail'),
    path('discotecas/<int:discoteca_id>/complete', views.complete_discoteca, name='complete_discoteca'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    

]
