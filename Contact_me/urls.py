from django.urls import path
from Contact_me import views

urlpatterns = [
    path('', views.contact , name="contact"),
]