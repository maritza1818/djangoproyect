from django.contrib import admin
from .models import Discoteca, Project

class DiscotecaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'horario_apertura', 'horario_cierre', 'user')  # Agregado 'usuario'

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'important', 'discoteca')  # Agregado 'discoteca'

admin.site.register(Discoteca, DiscotecaAdmin)
admin.site.register(Project, ProjectAdmin)
