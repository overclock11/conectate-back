from unittest import TestCase
from django.conf import settings
from rest_framework.test import APIRequestFactory
from django.test import Client


class TestHomeApp(TestCase):
    def testService(self):
        c = Client()
        response = c.get('/api/tool/')
        self.assertEqual(response.status_code, 200)
