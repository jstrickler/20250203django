from django.http import HttpResponse
from .models import Superhero

def home(request):
    """
    Home page of the Superheroes app

    :param request: HTTP request
    :return: HTTP Response with displayable text
    """
    return HttpResponse("Welcome to the superhero app")

def hero(request, hero_name):
    """
    Display name and secret identity

    :param request: HTTP request
    :param hero_name: name of hero (str)
    :return: HTTP Response with displayable text
    """
    s = Superhero.objects.get(name=hero_name)
    return HttpResponse(
        "{} is really {}".format(s.secret_identity, s.name)
    )

