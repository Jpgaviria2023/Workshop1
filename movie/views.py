from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def home(request):
    # Obtener lo que el usuario escribió en la barra de búsqueda
    searchTerm = request.GET.get('searchMovie', '')

    # Si hay término de búsqueda, filtrar por título
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    # Renderizar la plantilla con los datos
    return render(request, 'home.html', {
        'searchTerm': searchTerm,
        'movies': movies
    })


def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')
