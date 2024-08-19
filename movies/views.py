from django.shortcuts import render
import requests
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.conf import settings


def home(request):
    api_key = settings.OMDB_API_KEY
    fav_movie='Jab We Met'
    url= f'https://www.omdbapi.com/?s={fav_movie}&apikey={api_key}&page=1'
    response=requests.get(url)
    movies=response.json().get('Search',[])
    return render(request,'movie.html',{'movies':movies})

def details(request,title):
    api_key=settings.OMDB_API_KEY
    url= f'https://www.omdbapi.com/?t={title}&apikey={api_key}&page=1'
    response=requests.get(url)
    movie_det=response.json()
    return JsonResponse(movie_det)