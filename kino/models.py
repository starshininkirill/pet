from django.db import models


class Genre(models.Model):
   name = models.CharField(max_length=120, null=True, blank=True)

   def __str__(self):
      return self.name
   
   class Meta:
      verbose_name = 'Жанр'
      verbose_name_plural = 'Жанры'

class Film(models.Model):
   name = models.CharField(max_length=120, null=True, blank=True)
   genres = models.ManyToManyField(Genre)
   
   def __str__(self):
      return self.name
   
   class Meta:
      verbose_name = 'Фильм'
      verbose_name_plural = 'Фильмы'