from django.db import models


class Director(models.Model):
    name = models.CharField(help_text='Ingrese el nombre del director', max_length=64)
    surname = models.CharField(help_text='Apellidos del director', max_length=64)
    born = models.DateField()
    die = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.surname


class Films(models.Model):
    title = models.CharField(help_text='Titulo de la pelicula', max_length=32)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(help_text='De qué es la pelicula', max_length=400)
    release = models.DateField()

    def __str__(self):
        return self.title

