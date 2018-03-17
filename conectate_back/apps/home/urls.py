from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from apps.home.views import *

urlpatterns =[
    path('superheroes/',SuperHeroesListAll.as_view()),
    path('superheroes/<superheroe_name>',SuperHeroesList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)