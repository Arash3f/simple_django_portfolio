from Project.models import Project
from django.contrib import admin

@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display  = ['title']