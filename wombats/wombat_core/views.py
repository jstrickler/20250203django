from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render

# example without template (only used in class -- always use templates in real life):
def home(request):
    response = HttpResponse("Welcome to Wombat Core")
    response.status_code=404
    response.headers.setdefault('x-silly-header', 'goofus')
    return response


# example with template (normal Django approach)
# def home(request):
#     context = { 'message': "Welcome to Wombat Core" }
#     return render(request, 'wombat_core/home.html', context)
