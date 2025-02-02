"""
URL Configuration for superheroes
"""
from django.urls import path
from . import views   # import views from app

app_name = 'superheroes'

urlpatterns = [
    path('', views.home, name='home'),
    path(
        'herohardway/<str:hero_name>/',
        views.hero_hard_way,
        name="herohardway",
    ),
    path(
        'heroeasyway/<str:hero_name>/',
        views.hero_easy_way,
        name="heroeasyway",
    ),
    path(
        'herolookups/<str:hero_name>/',
        views.hero_lookups,
        name="herolookups",
    ),
    path(
        'herofilters/<str:hero_name>/',
        views.hero_filters,
        name="herofilters",
    ),
    path(
        'herotags/<str:hero_name>/',
        views.hero_tags,
        name="herotags",
    ),
    path(
        'herodetails/<str:hero_name>/',
        views.hero_details,
        name="herodetails",
    ),
    path(
        'heroescape/<str:hero_name>/',
        views.hero_escape,
        name="heroescape",
    ),
    path(
        'herourls/',
        views.hero_urls,
        name="herourls",
    ),
    path(
        'herostatic/<str:hero_name>/',
        views.hero_static,
        name="herostatic",
    ),
]

