from django.urls import path
from . import views

urlpatterns =[
    path('',views.admin,name='home'),
    path('details/<str:title>/',views.details,name='details'),
    path('searched/',views.searched,name='searched')
]