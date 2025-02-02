from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Band, Genre


def home(request):
    return HttpResponse("Welcome to the Bands app")


def band_basic(request, band_name):
    band = Band.objects.get(name=band_name)
    data = {'band': band}
    return render(request, 'bands/band_basic.html', data)


def bands_list(request):
    bands = Band.objects.all()
    data = {'bands': bands, 'title': 'Bands'}
    return render(request, 'bands/bands_list.html', data)

def bands_sorted(request):
    bands = Band.objects.all().order_by('name')
    data = {'bands': bands, 'title': 'Bands'}
    return render(request, 'bands/bands_list.html', data)

def band_details(request, pk):
    band = Band.objects.get(pk=pk)
    data = {'band': band}
    return render(request, 'bands/band_details.html', data)


def bands_by_genre(request, genre_name):
    bands = Band.objects.filter(genre__name__icontains=genre_name)
    data = {'genre': genre_name, 'bands': bands, 'title': 'Bands'}
    return render(request, 'bands/bands_list.html', data)


def bands_search(request, search_term):
    bands = Band.objects.all().filter(name__icontains=search_term)
    data = {'bands': bands, 'title': 'Bands'}
    return render(request, 'bands/bands_list.html', data)

# chapter 9
def bands_list_more(request):
    bands = Band.objects.all()
    data = {'bands': bands, 'title': 'Bands'}
    return render(request, 'bands/bands_list_more.html', data)
