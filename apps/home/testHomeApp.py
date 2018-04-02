from unittest import TestCase
from django.conf import settings
from rest_framework.test import APIRequestFactory


class TestHomeApp(TestCase):
    def testService(self):
        settings.configure()
        factory = APIRequestFactory()
        request = factory.get('/tools/')
        print(request)
