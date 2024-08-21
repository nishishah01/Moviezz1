from django.shortcuts import render
from .models import Moviee
import requests
from django.conf import settings

def details(request):
    api_key = settings.OMDB_API_KEY
    fav_movie = request.GET.get('title')
    if fav_movie:
        url = f'https://www.omdbapi.com/?t={fav_movie}&apikey={api_key}&page=1'
        response = requests.get(url)
        movie_data = response.json()
        print(movie_data)


        movie, created = Moviee.objects.get_or_create(
            title=movie_data['Title'],
            year=movie_data['Year'],
            genre=movie_data['Genre'],
            plot=movie_data['Plot'],
            poster=movie_data['Poster'],
        )
        movie.search += 1
        movie.save()

        return render(request, 'movie.html', {'movies': movie_data})

    return render(request, 'movie.html', {'movies': []})


def searched(request):
    movies=Moviee.objects.all()
    return render(request, 'searched.html',{'movies': movies})