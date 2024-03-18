from django.urls import path
from kino.views import films

app_name = 'kino'

urlpatterns = [
    path('films/', films, name='films'),
]