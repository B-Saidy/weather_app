from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class News(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'media/photos')
    content =  RichTextUploadingField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = 'News'
        
    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'media/photos')
    content =  RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
            
    def __str__(self):
        return self.title