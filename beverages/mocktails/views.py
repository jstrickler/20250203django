from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request): # incoming HTTPRequest object
    return HttpResponse("Welcome to the Mocktail app")

def drinklist(request): 
    return HttpResponse("menu of mocktails")
