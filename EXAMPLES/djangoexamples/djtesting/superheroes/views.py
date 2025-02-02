from django.shortcuts import render, get_object_or_404
from .models import Superhero

def home(request):
    superheroes = Superhero.objects.all()
    data = {'superheroes': superheroes}
    return render(request, 'superheroes/home.html', data)



def hero_details(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    data = {
        'hero': hero,
    }
    return render(request, 'superheroes/hero_details.html', data)
