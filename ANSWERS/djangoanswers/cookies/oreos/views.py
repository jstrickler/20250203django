from django.http import HttpResponse

def home(request):
    return HttpResponse("Dunk me in milk!!")

