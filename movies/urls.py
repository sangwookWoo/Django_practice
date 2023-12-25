from django.urls import path

from .views import actor_list, movie_list

urlpatterns = [path("movies", movie_list), path("actors", actor_list)]
