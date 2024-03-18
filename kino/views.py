from django.shortcuts import render
from django.http import HttpResponse

from kino.models import Genre, Film


def main_page(request):
    films = Film.objects.all()
    context = {
        'page_title': 'Главная',
        'films': films
    }
    return render(request, template_name='kino/index.html', context=context)


def films(request):
    films = Film.objects.all()
    context = {
        'page_title': 'Фильмы',
        'films': films
    }
    return render(request, 'kino/movies.html', context=context)