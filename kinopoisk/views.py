from django.shortcuts import render
from django.http import  HttpResponse


def main_page(request):
    return render(request, template_name='kino/index.html')


def test(request):
    return HttpResponse('test')