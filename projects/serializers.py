from rest_framework import serializers
from .models import Project

class ProjectSerializer (serializers.ModelSerializer):
    class Meta:
        models = Project
        fields = ('id','title', 'description', 'technology' , 'created_at')
        read_only_fields = ('create_at',)