from django.urls import path

from .views import actor_list, movie_detail, movie_list

urlpatterns = [
    path("movies", movie_list),
    path("movies/<int:pk>", movie_detail),
    path("actors", actor_list),
]
