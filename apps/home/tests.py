from unittest import TestCase
from django.conf import settings
from rest_framework.test import APIRequestFactory
from django.test import Client
from apps.home.views import  *

object_created_status_code = 201
ok_status_code = 200

client = Client()
BASE_TOOLS_URL = '/api/tool/'
BASE_TUTORIALS_URL = '/api/tutorial/'
BASE_EXAMPLES_URL = '/api/example/'

def to_string(id):
    if (isinstance(id, int)):
        return str(id)
    else:
        return id


def api_url_for_base_with_id(base_url, id):
    return base_url + to_string(id) + '/'


class TestToolAPI(TestCase):
    base_url = BASE_TOOLS_URL

    def get_all_tools(self):
        response = client.get(self.base_url)
        return response.json()

    def test_all_tool_retrieval(self):
        response = client.get(self.base_url)
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
        response = client.post(self.base_url, data=data, content_type='application/json')
        #print("\ncontent = {}".format(response.json()))
        self.assertEqual(response.status_code, object_created_status_code)

    def test_tool_retrieval_with_ID(self):
        response = client.get(api_url_for_base_with_id(self.base_url, 1))
        self.assertEqual(response.status_code, ok_status_code)

    def test_tool_update_with_ID(self):
        data = '''{
            "name": "New name",
            "description": "New description",
            "state": "New state"
        }'''
        response = client.put(api_url_for_base_with_id(self.base_url, 1), data=data, content_type='application/json')
        self.assertEqual(response.status_code, ok_status_code)

    def test_tool_get_associated_examples(self):
        response = client.get(api_url_for_base_with_id(self.base_url, 1) + 'examples/')
        self.assertEqual(response.status_code, ok_status_code)

    def test_tool_get_associated_tutorials(self):
        response = client.get(api_url_for_base_with_id(self.base_url, 1) + 'tutorials/')
        self.assertEqual(response.status_code, ok_status_code)

class TestTutorialAPI(TestCase):
    base_url = BASE_TUTORIALS_URL

    def test_all_tutorials_retrieval(self):
        response = client.get(self.base_url)
        self.assertEqual(response.status_code, ok_status_code)

    def test_tutorial_creation(self):
        data = '''{
            "name": "Mi tutorial",
            "objective": "Este es un tutorial para probar la base de datos",
            "url": "http://www.tutorialdeprueba.org/guia.pdf",
            "tool": 1
        }'''
        response = client.post(self.base_url, data=data, content_type='application/json')
        #print("\ncontent = {}".format(response.json()))
        self.assertEqual(response.status_code, object_created_status_code)

    def test_tutorial_retrieval_with_ID(self):
        response = client.get(api_url_for_base_with_id(self.base_url, 1))
        self.assertEqual(response.status_code, ok_status_code)

    def test_tutorial_update_with_ID(self):
        data = '''{
            "name": "NUEVO Tutorial",
            "objective": "¡Nuevo objetivo!",
            "url": "http://newurl.com"
        }'''
        response = client.put(api_url_for_base_with_id(self.base_url, 1), data=data, content_type='application/json')
        self.assertEqual(response.status_code, ok_status_code)