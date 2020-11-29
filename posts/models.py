from django.db import models
import datetime as dt 

from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Image (models.Model):
    project_title=models.CharField(max_length=50)
    project_description = models.TextField()
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(default="default.jpeg", upload_to = 'images/')
    project_link=models.CharField(max_length=50, null=False)
    
class ProjectsApi (models.Model):
    project_title=models.CharField(max_length=50)
    project_description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(default="default.jpeg", upload_to = 'images/')


class ProfileApi(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image=models.ImageField(default="profile_pics/default.jpeg", upload_to='profile_pics')
    bio=models.CharField(max_length=200, blank=False)
    contact_information = models.TextField()
    
    
    
    
    
    
    