from unittest import TestCase
from django.conf import settings
from rest_framework.test import APIRequestFactory
from django.test import Client
from apps.home.views import  *

from apps.home.models import *

object_created_status_code = 201
ok_status_code = 200

client = Client()
BASE_TOOLS_URL = '/api/tool/'
BASE_STRATEGIES_URL = '/api/pedagogic_strategy/'
BASE_TUTORIALS_URL = '/api/tutorial/'

class TestToolAPI(TestCase):
    def get_all_tools(self):
        response = client.get(BASE_TOOLS_URL)
        return response.json()

    def test_all_tool_retrieval(self):
        response = client.get(BASE_TOOLS_URL)
        print("\ncontent = {}".format(response.json()))
        self.assertEqual(response.status_code, ok_status_code)

    def test_tool_creation(self):
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
        response = client.post(BASE_TOOLS_URL, data=data, content_type='application/json')
        #print("\ncontent = {}".format(response.json()))
        self.assertEqual(response.status_code, object_created_status_code)

    def test_tool_retrieval_with_ID(self):
        response = client.get(BASE_TOOLS_URL + '1/')
        self.assertEqual(response.status_code, ok_status_code)

    def test_tool_update_with_ID(self):
        data = '''{
            "name": "New name",
            "description": "New description",
            "state": "New state"
        }'''
        response = client.put(BASE_TOOLS_URL + '1/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, ok_status_code)

class TestTutorialAPI(TestCase):
    def api_url_for_tutorial_with_ID(self, id):
        id_string = ''
        if(isinstance(id, int)):
            id_string = str(id)
        else:
            id_string = id
        return BASE_TUTORIALS_URL + id_string + '/'

    def test_all_tutorials_retrieval(self):
        response = client.get(BASE_TUTORIALS_URL)
        self.assertEqual(response.status_code, ok_status_code)

    def test_tutorial_creation(self):
        data = '''{
            "name": "Mi tutorial",
            "objective": "Este es un tutorial para probar la base de datos",
            "url": "http://www.tutorialdeprueba.org/guia.pdf",
            "tool": 1
        }'''
        response = client.post(BASE_TUTORIALS_URL, data=data, content_type='application/json')
        #print("\ncontent = {}".format(response.json()))
        self.assertEqual(response.status_code, object_created_status_code)

    def test_tutorial_retrieval_with_ID(self):
        response = client.get(self.api_url_for_tutorial_with_ID(1))
        self.assertEqual(response.status_code, ok_status_code)

    def test_tutorial_update_with_ID(self):
        data = '''{
            "name": "NUEVO Tutorial",
            "objective": "¡Nuevo objetivo!",
            "url": "http://newurl.com"
        }'''
        response = client.put(self.api_url_for_tutorial_with_ID(1), data=data, content_type='application/json')
        self.assertEqual(response.status_code, ok_status_code)


class TestStrategyAPI(TestCase):
    def test_get_all_strategies(self):
        response = client.get(BASE_STRATEGIES_URL)
        self.assertEqual(response.status_code, ok_status_code)

    def test_strategy_create(self):
        new_object = PedagogicStrategy()
        new_object.name = 'Test Strategy'
        data = PedagogicStrategySerializer(new_object).data
        response = client.put(BASE_STRATEGIES_URL + '1/', data=data, content_type='application/json')
        created_object = PedagogicStrategySerializer.create(response.body)
        self.assertEqual(new_object.name, created_object.name)

