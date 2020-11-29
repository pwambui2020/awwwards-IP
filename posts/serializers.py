from rest_framework import serializers
from .models import ProjectsApi
from .models import ProfileApi


class ProjectSerializer(serializers.ModelSerializer):
    class meta:
        model = ProjectsApi
        fields = ('id', 'user', 'profile_image', 'bio', 'contact_information')
        
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class meta:
        model = ProfileApi
        fields = ('id', 'project_title', 'project_description', 'profile', 'pub_date', 'project_image')
        