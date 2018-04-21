from unittest import TestCase
from django.conf import settings
from rest_framework.test import APIRequestFactory
from django.test import Client
from apps.home.views import  *

object_created_status_code = 201
ok_status_code = 200

class TestHomeApp(TestCase):
    client = Client()
    BASE_TOOLS_URL = '/api/tool/'
    BASE_TUTORIALS_URL = '/api/tutorial/'

    def get_all_tools(self):
        response = self.client.get(self.BASE_TOOLS_URL)
        return response.json()

    def testAllToolsRetrieval(self):
        response = self.client.get(self.BASE_TOOLS_URL)
        print("\ncontent = {}".format(response.json()))
        self.assertEqual(response.status_code, ok_status_code)

    def testToolCreation(self):
        data = '''{
            "name": "Test Tool",
            "description": "This tool was created as part of a Unit Test",
            "url_site": "www.test.org",
            "url_download": "amazon.s3.fafwemwewfwc.com",
            "usage_restrictions": "No puede ser instalado en más de 100 computadores",
            "license_type": "Payed",
            "version": "0.2a",
            "key_words": "test, unit",
            "state": "Publicada",
            "integracion_lms": "None"
        }'''
        response = self.client.post(self.BASE_TOOLS_URL, data=data, content_type='application/json')
        #print("\ncontent = {}".format(response.json()))
        self.assertEqual(response.status_code, object_created_status_code)

    def testToolRetrievalWithID(self):
        response = self.client.get(self.BASE_TOOLS_URL + '1/')
        self.assertEqual(response.status_code, ok_status_code)

    def testToolUpdateWithID(self):
        data = '''{
            "name": "New name",
            "description": "New description",
            "state": "New state"
        }'''
        response = self.client.put(self.BASE_TOOLS_URL + '1/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, ok_status_code)

    def testAllTutorialsRetrieval(self):
        response = self.client.get(self.BASE_TUTORIALS_URL)
        self.assertEqual(response.status_code, ok_status_code)

    def testTutorialCreation(self):
        data = '''{
            "name": "Mi tutorial",
            "objective": "Este es un tutorial para probar la base de datos",
            "url": "tutorialdeprueba.org/guia.pdf",
            "tool": 1
        }'''
        response = self.client.post(self.BASE_TUTORIALS_URL, data=data, content_type='application/json')
        #print("\ncontent = {}".format(response.json()))
        self.assertEqual(response.status_code, object_created_status_code)

    def testTutorialRetrievalWithID(self):
        response = self.client.get(self.BASE_TUTORIALS_URL + '1/')
        self.assertEqual(response.status_code, ok_status_code)

    def testTutorialUpdateWithID(self):
        data = '''{
            "name": "NUEVO Tutorial",
            "objective": "¡Nueva descripción!"
        }'''
        response = self.client.put(self.BASE_TUTORIALS_URL+ '1/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, ok_status_code)