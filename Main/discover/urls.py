"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('discover', views.discover),
    path('newsfeed', views.newsfeed,name = 'newsfeed'),
    path('Follower', views.follower,name = 'follower'),
    path('Following', views.following,name = 'following'),
    path('discover_more', views.discover_more, name='discover_more'),
    path('get_search', views.get_search, name='get_search'),
    path('get_location', views.get_location, name='get_location'),
    path('search', views.search)
]
