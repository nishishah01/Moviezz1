from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('movie/<str:title>/',views.details,name='details'),
]