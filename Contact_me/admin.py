from django.contrib import admin
from Contact_me.models import Contact

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display  = ['__str__' ,'email']