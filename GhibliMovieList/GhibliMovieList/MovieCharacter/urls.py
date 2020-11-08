from django.urls import path, include
from .views import (CreateProductViewSets, ListProductViewSets,
                    UpdateProductViewSets, SearchProductViewSets, ListProductArticlesViewSets)
from django_filters.views import FilterView


urlpatterns = [
    path('add', CreateProductViewSets.as_view()),

]