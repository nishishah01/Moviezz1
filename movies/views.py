from django.shortcuts import render
import requests
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.conf import settings
import random


def home(request):
    api_key = settings.OMDB_API_KEY
    fav_movie='Harry Potter'
    url= f'https://www.omdbapi.com/?s={fav_movie}&apikey={api_key}&page=1'
    response=requests.get(url)
    movies=response.json().get('Search',[])
    

    #task2
    genre=request.GET.get('genre')
    print(genre)
    if genre:
        genreUrl= f'https://www.omdbapi.com/?s={genre}&apikey={api_key}&page=1'
        genreResponse = requests.get(genreUrl)

        genreMovie=genreResponse.json().get('Search',[])
        movies=[movie for movie in genreMovie if genre.lower() in movie.get('Genre',' ').lower()]
        print(genreResponse)
    return render(request,'movie.html',{'movies':movies})


def details(request,title):
    api_key=settings.OMDB_API_KEY
    url= f'https://www.omdbapi.com/?t={title}&apikey={api_key}&page=1'
    response=requests.get(url)
    movie_det=response.json()
    return JsonResponse(movie_det)