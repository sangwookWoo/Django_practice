from django.urls import path

from .views import actor_detail, actor_list, movie_detail, movie_list

urlpatterns = [
    path("movies", movie_list),
    path("movies/<int:pk>", movie_detail),
    path("actors", actor_list),
    path("actors/<int:pk>", actor_detail),
]
