from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from apps.home.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tool', ToolList)
router.register(r'example', ExampleList)

urlpatterns = [
    path('api/', include(router.urls)),
    path('tutorial', TutorialList.as_view()),
]
