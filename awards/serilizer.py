from rest_framework import serializers
from .models import *

class ProjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('project_name', 'project_photo', 'description', 'github_repo', 'url',)