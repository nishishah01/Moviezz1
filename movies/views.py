from django.shortcuts import render
from .models import Moviee
import requests
from django.conf import settings

def details(request):
    api_key = settings.OMDB_API_KEY
    fav_movie = request.GET.get('fav_movie', ' ')
    url = f'https://www.omdbapi.com/?t={fav_movie}&apikey={api_key}&page=1'
    response = requests.get(url)
    movie_data = response.json()


    movie, created = Moviee.objects.get_or_create(
        title=movie_data['Title'],
        defaults={
            'year': movie_data.get('Year'),
            'genre': movie_data.get('Genre'),
            'plot': movie_data.get('Plot'),
            'poster': movie_data.get('Poster'),
            
        }
    )

    if not created:

        movie.search_count += 1
        movie.save()

    return render(request, 'movie.html', {'movies': [movie]})

def searched(request):
    movies=Moviee.objects.all()
    return render(request, 'searched.html',{'movies': movies})