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
    content =  RichTextUploadingField()
    date_posted = models.DateTimeField(default=timezone.now)
            
    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'media/photos')
    content =  RichTextUploadingField()        
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company_name = models.CharField(max_length=150)
    text = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Media(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to = 'media/photos')
    content =  models.TextField(max_length = 250, null=True, blank=True)  
    class Meta:
        verbose_name_plural = 'Media'      
    def __str__(self):
        return self.title


