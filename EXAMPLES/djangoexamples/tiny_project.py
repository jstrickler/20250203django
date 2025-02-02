"""
Unrealistically minimum Django app. Combines manage.py, settings.py, views.py, and urls.py into a single file.

Definitely not recommended for real-world apps.
"""
import os
import sys
from django.urls import path
from django.http import HttpResponse

DEBUG = True

ROOT_URLCONF = 'tiny_project'

def hello(request):
    return HttpResponse("Hello really tiny Django world")

urlpatterns = [ path('', hello) ]

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tiny_project")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv + ['runserver'])
