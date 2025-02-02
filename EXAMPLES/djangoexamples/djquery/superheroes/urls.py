"""
URL Configuration for superheroes
"""
from django.urls import path
from .views import home

app_name = 'superheroes'

urlpatterns = [
    path('', home, name='home'),
]
