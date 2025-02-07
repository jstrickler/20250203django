"""
URL Configuration for djplot_core
"""
from django.urls import path
from . import views   # import views from app

app_name = "djplot_core"

urlpatterns = [
    # add url patterns for the djplot_core app here

    # Examples:
    path('', views.home, name='home'),
    path('simpleplot', views.simpleplot, name='simpleplot'),
    path('babyplot', views.babyplot, name='babyplot')
]
