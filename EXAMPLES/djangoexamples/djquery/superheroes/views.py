from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, Count, Min, Max
from .models import Superhero

Q_DEADPOOL = Q(name__icontains="dead")
Q_WOMAN = Q(name__icontains="woman")


def home(request):
    context = {
        'page_title': 'Query Examples',
    }

    context['all'] = Superhero.objects.all()
    context['superman'] = Superhero.objects.filter(name="Superman")
    context['superman_first'] = Superhero.objects.filter(name="Superman").first()
    context['spiderman_first_id'] = Superhero.objects.filter(name="Spider-Man").first().secret_identity
    context['superman_enemies_all'] = Superhero.objects.filter(name="Superman").first().enemies.all
    context['spiderman_get_powers_all'] = Superhero.objects.get(name="Spider-Man").powers.all
    context['exclude_ww'] = Superhero.objects.exclude(name="Wonder Woman")
    context['all_order_by'] = Superhero.objects.order_by("name")
    context['all_count'] = Superhero.objects.count()
    context['agg_count'] = Superhero.objects.aggregate(Count("name"))
    context['agg_min'] = Superhero.objects.aggregate(Min("name"))
    context['agg_max'] = Superhero.objects.aggregate(Max("secret_identity"))
    context['agg_minmax'] = Superhero.objects.aggregate(Min("name"),Max("name"))
    context['contains'] = Superhero.objects.filter(name__icontains="man")
    context['contains_count'] = Superhero.objects.filter(name__icontains="man").count()
    context['contains_exclude'] = Superhero.objects.filter(name__icontains="man").exclude(name__icontains="woman")
    context['contains_exclude_count'] = Superhero.objects.filter(name__icontains="man").exclude(name__icontains="woman").count()
    context['all_slice'] = Superhero.objects.all()[:3]
    context['contains_slice'] = Superhero.objects.filter(name__icontains="man")[:2]
    context['enemies_icontains_name'] = Superhero.objects.filter(enemies__name__icontains="Luthor").first().name
    context['filter_q'] = Superhero.objects.filter(Q_DEADPOOL | Q_WOMAN)

    return render(request, 'superheroes/hero_queries.html', context)



