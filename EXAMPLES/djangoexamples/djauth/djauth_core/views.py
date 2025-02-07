from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        message = "You are logged in"
    else:
        message = "You are NOT logged in"
    context = {"message": message, 'user': request.user, "homepage": True}
    return render(request, "djauth_core/home.html", context)

@login_required(login_url='/users/login/')
def private1(request):
    context = {'message': 'Only logged-in users can see this',
                        'heading': 'Private Page 2'}
    return render(request, "djauth_core/common.html", context=context)

class private2(LoginRequiredMixin, TemplateView):
    # used to provide context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'message': 'Only logged-in users can see this',
                        'heading': 'Private Page 2'})
        return context

    template_name = "djauth_core/common.html"
    login_url = "/users/login/"

# anyone can see this
def public1(request):
    context = {'message': 'Anyone can see this', 'heading': 'Public Page 1'}
    return render(request, "djauth_core/common.html", context=context)