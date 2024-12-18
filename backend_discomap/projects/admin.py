from django.contrib import admin
from .models import Discoteca, Project, Evento, UserProfile

class DiscotecaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'horario_apertura', 'horario_cierre', 'user')  # Agregado 'usuario'

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'important', 'discoteca')  # Agregado 'discoteca'
    readonly_fields = ("created_at",)

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'hora_inicio', 'hora_fin', 'discoteca', 'creador', 'created_at')
    search_fields = ('nombre', 'descripcion', 'discoteca__nombre', 'creador__username')
    list_filter = ('fecha', 'hora_inicio', 'discoteca')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'gender', 'email_notifications', 'push_notifications')
    search_fields = ('user__username', 'personal_phrase')
    list_filter = ('gender', 'email_notifications', 'push_notifications')

admin.site.register(Discoteca, DiscotecaAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
