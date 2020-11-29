from django.db import models
import datetime as dt 

# Create your models here.
class Image (models.Model):
    project_title=models.CharField(max_length=60)
    project_description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(default="default.jpeg", upload_to = 'images/')
    project_link=models.CharField(max_length=60, null=False)
    
