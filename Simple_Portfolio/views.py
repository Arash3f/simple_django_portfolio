from django.shortcuts import render
from Account.models import (
    User , 
    Skill , 
    Experience , 
    Service
)
from Project.models import Project
from Contact_me.forms import messageform

def handler404(request, exception):
    template_name="error_404.html"
    return render(request,template_name)

def index(request):
    template_name="index.html"
    data={
        'user' : User.objects.all()[0],
        'skills':Skill.objects.all(),
        'experience' : Experience.objects.all(),
        'services' : Service.objects.all(),
        'projects' : Project.objects.all(),
        'form': messageform(None)
    }
    return render(request,template_name , context=data)