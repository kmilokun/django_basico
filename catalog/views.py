from django.shortcuts import render
from .models import *
# from .templates import *

def index(request):
    num_directors = Director.objects.all().count()
    num_films = Films.objects.all().count()
    return render(
        request, 'index.html',
        context={
            'num_directors': num_directors,
            'num_films': num_films
        }
    )
def films(request):
    num_directors = Director.objects.all().count()
    num_films = Films.objects.all().count()
    return render(
        request, 'films.html',
        context={
            'num_directors': num_directors,
            'num_films': num_films
        }
    )