from django.contrib import admin
# Register your models here.

from .models import Band, Genre, Member

for model in Band, Genre, Member:
    admin.site.register(model)
