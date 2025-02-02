"""
URL Configuration for oreos
"""
from django.urls import path
from . import views   # import views from app

app_name = "oreos"

urlpatterns = [
    path('', views.home, name='home'),
]
