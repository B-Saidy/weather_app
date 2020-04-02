from django.db import models
from django.utils import timezone


class News(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'media/photos')
    content = models.TextField(max_length=None)
    date_posted = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = 'News'
        
    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'media/photos')
    content = models.TextField(max_length=None)
    date_posted = models.DateTimeField(default=timezone.now)
            
    def __str__(self):
        return self.title