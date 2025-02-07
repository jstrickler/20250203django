from django.contrib import admin
# Register your models here.

from .models import Superhero, City, Power, Enemy
from .models_plus import SuperheroPlus, CityPlus, PowerPlus, EnemyPlus

for model in Superhero, City, Power, Enemy:
    admin.site.register(model)

for model in SuperheroPlus, CityPlus, PowerPlus, EnemyPlus:
    admin.site.register(model)
