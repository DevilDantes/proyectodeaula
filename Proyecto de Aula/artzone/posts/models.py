from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True) 
