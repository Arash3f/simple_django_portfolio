from Contact_me import models
from django import forms
from django.core.exceptions import ValidationError

class messageform(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields ='__all__'
        widgets = {
            'name'   : forms.TextInput(attrs={'class':"form-control" , "type":"text" , "id":"name" , "name":"name" , "placeholder":"Enter your name"}),
            'email'  : forms.TextInput(attrs={'class':"form-control" , "type":"email" , "id":"email" , "name":"email" , "placeholder":"Enter your email"}),
            'subject': forms.TextInput(attrs={'class':"form-control" , "type":"text" , "id":"subject" , "name":"subject" , "placeholder":"Enter subject"}),
            'memessages': forms.Textarea(attrs={'class': "form-control" , "id":"message" , "name":"message" , "placeholder":"Enter message"}),
        }

    def clean(self):
        cd = self.cleaned_data
        email = cd.get('email')
        name = cd.get('name')
        subject = cd.get('subject')
        message = cd.get('message')
        if email=="" :
            raise ValidationError("ValidationError")
        elif name=="":
            raise ValidationError("ValidationError")
        elif message=="":
            raise ValidationError("ValidationError")
        elif subject=="":
            raise ValidationError("ValidationError")
            
        return cd
    