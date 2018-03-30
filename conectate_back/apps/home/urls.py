from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from apps.home.views import *

urlpatterns =[
    path('tools/',ToolList.as_view()),
    path('tool/',SuperHeroesListAll.as_view()),
    path('tutorials', TotorialList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)