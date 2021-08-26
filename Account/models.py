from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class User(models.Model):
    user         = models.OneToOneField( User , related_name='user',  on_delete=models.CASCADE)
    picture      = models.ImageField  ( 'user_pictures' , upload_to='user_pictures/' , blank=True , null=True)
    about_me     = models.TextField()
    job          = models.CharField   ( 'Job'       , max_length=30 , blank=True , null=True)
    date_of_birth= models.DateField   ( 'Date of birth' , blank=True , null=True)
    github       = models.CharField   ( 'Github'    , max_length=100 , blank=True , null=True)
    skype        = models.CharField   ( 'Skype'  , max_length=100 , blank=True , null=True)
    twitter      = models.CharField   ( 'Twitter'   , max_length=100 , blank=True , null=True)
    instagram    = models.CharField   ( 'Instagram' , max_length=100 , blank=True , null=True)

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.user.username

class Skill(models.Model):
    title  = models.CharField   ( 'Title'  , max_length=30 , blank=True , null=True)
    amount = models.IntegerField( 'Amount' , default=0 , blank=True , null=True)
    
    class Meta:
        verbose_name = ("Skill")
        verbose_name_plural = ("Skills")
    
    def __str__(self):
        return self.title
    
class Experience(models.Model):
    title  = models.CharField( 'Title' , max_length=30 , blank=True , null=True)
    body   = models.TextField( 'About',max_length=500 , blank=True  , null=True )
    Date   = models.DateField( 'Date' , blank=True , null=True)
    picture= models.ImageField('user_experience' , upload_to='experience_pictures/' , blank=True , null=True)
    
    class Meta:
        verbose_name = ("Experience")
        verbose_name_plural = ("Experiences")
    
    def __str__(self):
        return self.title
    
class Service(models.Model):
    title     = models.CharField( 'Title' , max_length=30 , blank=True , null=True)
    about     = models.TextField()
    
    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")
        
    def __str__(self):
        return self.title