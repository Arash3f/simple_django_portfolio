from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

class Project(models.Model):
    title   = models.CharField( 'Title' , max_length=30 , blank=True , null=True)
    about   = models.TextField()
    picture = models.ImageField('projects' , upload_to='project_pictures/' , blank=True , null=True)

    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")

    def __str__(self):
        return f"{self.title}"

    
    
    
    
    