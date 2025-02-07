import os
from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Line
import pandas as pd
from .forms import BabyNameForm

BABYNAMES = pd.read_csv('../../../DATA/baby-names.csv')
MIN_PERCENT = BABYNAMES['percent'].min()
MAX_PERCENT = BABYNAMES['percent'].max()
MIN_YEAR = BABYNAMES['year'].min()
MAX_YEAR = BABYNAMES['year'].max()

def home(request):
    context = { 
        'homepage': True,
        'message': "Welcome to Django Plot Demo Core",
    }
    return render(request, 'djplot_core/home.html', context)

def simpleplot(request):
    x_data = list(range(10))
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    
    return render(request, "djplot_core/simpleplot.html", context={'plot_div': plot_div})

def babyplot(request):
    form = BabyNameForm()
    context = {'form': form}
    if request.method == 'GET':
        return render(request, 'djplot_core/babyplot.html', context)
    else:
        form = BabyNameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'].title()
            sex = form.cleaned_data['sex']
            plot_div = get_baby_plot(name, sex)
            return render(request, "djplot_core/babyplot.html", context={
                'title': "baby names",
                'heading': "Baby names popularity",
                'form': form,
                'plot_div': plot_div,
            })
        else:
            return render(request, 'djplot_core/babyplot.html', context)

def get_baby_plot(name, sex):
    df_name = BABYNAMES[(BABYNAMES.name == name) & (BABYNAMES.sex == sex)]

    x_data = df_name['year']
    y_data = df_name['percent']
    div = plot(
        {
            'data': [
                Scatter(x=x_data, 
                        y=y_data, 
                        mode='lines', 
                        name='test',
                        opacity=0.8, 
                        marker_color='green')
            ],
            'layout': go.Layout(
                title=name,
                titlefont={'color': 'blue', 'family': 'arial',
                           'size': 32 },
                xaxis=go.XAxis(
                    title="year",
                    range=[MIN_YEAR, MAX_YEAR]
                ),
                yaxis=go.YAxis(
                    title="percentage",
                    range=[MIN_PERCENT, MAX_PERCENT]
                ),
            ),                
        },
        output_type='div'
    )
    return div