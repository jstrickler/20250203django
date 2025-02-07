"""
URL Configuration for djauth_core
"""
from django.urls import path
from . import views   # import views from app

app_name = "djauth_core"

urlpatterns = [
    path('', views.home, name='home'),
    path('private1', views.private1, name='private1'),
    path('private2', views.private2.as_view(), name='private2'),
    path('public1', views.public1, name='public1'),
]
