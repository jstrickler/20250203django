from django.contrib import admin

# Register your models here.

from superheroes.models import Superhero, Power, Enemy, City # import your models

admin.site.register(Superhero)  # register each model
admin.site.register(City)
admin.site.register(Enemy)

# customize the admin for this model
class PowerAdmin(admin.ModelAdmin):  # create custom Admin model
    search_fields = ['name', 'description'] # add Admin metadata

admin.site.register(Power, PowerAdmin) # register custom model
