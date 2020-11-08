from django.urls import path, include
from .views import CreateMovieViewSets
from django_filters.views import FilterView


urlpatterns = [
    path('movies', CreateMovieViewSets.as_view({'get' : 'list', 'post':'create'})),
   
]