"""
A Module to hold all the URL's for the contact app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact')
]
