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
BASE_RESOURCES_URL = '/api/resource/'


def to_string(id):
    if (isinstance(id, int)):
        return str(id)
    else:
        return id


def api_url_for_base_with_id(base_url, id):
    return base_url + to_string(id) + '/'

def get_all_elements_at_base(base_url):
    response = client.get(base_url)
    return response.json()

class TestToolAPI(TestCase):
    base_url = BASE_TOOLS_URL

    def test_all_tool_retrieval(self):
        response = client.get(self.base_url)
        print("\ncontent = {}".format(response.json()))
        number_of_retrieved_elements = len(response.json())
        self.assertEqual(response.status_code, ok_status_code)
        self.assertEqual(number_of_retrieved_elements, 0)

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
        numberOfStoredElements = len(get_all_elements_at_base(self.base_url))
        self.assertEqual(response.status_code, object_created_status_code)
        self.assertEqual(numberOfStoredElements, 1)

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


# class TestExampleAPI(TestCase):
#     base_url = BASE_EXAMPLES_URL
#
#     def test_all_examples_retrieval(self):
#         response = client.get(self.base_url)
#                 number_of_retrieved_elements = len(response.json())
#                 self.assertEqual(response.status_code, ok_status_code)
#                 self.assertEqual(number_of_retrieved_elements, 0)

#
#     def test_example_creation(self):
#         data = '''{
#             "name": "test ejemplo",
#             "description": "este ejemplo fue creado como una prueba",
#             "instructions": "para observar este ejemplo, es necesario tener al menos un ojo parcialmente funcional y un dispositivo con capacidades de computación",
#             "state": "Borrador",
#             "pedagogic_strategy": 1,
#             "discipline": 1,
#             "tool": 1
#         }'''
#         response = client.post(self.base_url, data=data, content_type='application/json')
#         numberOfStoredElements = len(get_all_elements_at_base(self.base_url))
#         self.assertEqual(response.status_code, object_created_status_code)
#         self.assertEqual(numberOfStoredElements, 1)
#
#     def test_example_retrieval_with_ID(self):
#         response = client.get(api_url_for_base_with_id(self.base_url, 1))
#         self.assertEqual(response.status_code, ok_status_code)
#
#     def test_example_update_with_ID(self):
#         data = '''{
#             "name": "test CHENJI",
#             "description": "test CHANGED",
#             "instructions": "Estas instrucciones difieren de las anteriores.",
#             "state": "Nuevo estado",
#             "pedagogic_strategy": 1,
#             "discipline": 1,
#             "tool": 1
#         }'''
#         response = client.put(api_url_for_base_with_id(self.base_url, 1), data=data, content_type='application/json')
#         self.assertEqual(response.status_code, ok_status_code)


# class TestResourceAPI(TestCase):
#     base_url = BASE_RESOURCES_URL
#
#     def test_all_resources_retrieval(self):
#         response = client.get(self.base_url)
#         number_of_retrieved_elements = len(response.json())
#         self.assertEqual(response.status_code, ok_status_code)
#         self.assertEqual(number_of_retrieved_elements, 0)
#
#     def test_resource_creation(self):
#         data = '''{
#             "name": "Guía de prueba",
#             "link": "http://link.com",
#             "example": 1
#         }'''
#         response = client.post(self.base_url, data=data, content_type='application/json')
#         numberOfStoredElements = len(get_all_elements_at_base(self.base_url))
#         self.assertEqual(response.status_code, object_created_status_code)
#         self.assertEqual(numberOfStoredElements, 1)
#
#     def test_resource_retrieval_with_ID(self):
#         response = client.get(api_url_for_base_with_id(self.base_url, 1))
#         self.assertEqual(response.status_code, ok_status_code)
#
#     def test_resource_update_with_ID(self):
#         data = '''{
#             "name": "Nuevo nombre de recurso",
#             "link": "http://nuevo-link-de-recurso.com",
#             "example": 1
#         }'''
#         response = client.put(api_url_for_base_with_id(self.base_url, 1), data=data, content_type='application/json')
#         self.assertEqual(response.status_code, ok_status_code)


class TestTutorialAPI(TestCase):
    base_url = BASE_TUTORIALS_URL

    def test_all_tutorials_retrieval(self):
        response = client.get(self.base_url)
        number_of_retrieved_elements = len(response.json())
        self.assertEqual(response.status_code, ok_status_code)
        self.assertEqual(number_of_retrieved_elements, 0)

    def test_tutorial_creation(self):
        data = '''{
            "name": "Mi tutorial",
            "objective": "Este es un tutorial para probar la base de datos",
            "url": "http://www.tutorialdeprueba.org/guia.pdf",
            "tool": 1
        }'''
        response = client.post(self.base_url, data=data, content_type='application/json')
        numberOfStoredElements = len(get_all_elements_at_base(self.base_url))
        self.assertEqual(response.status_code, object_created_status_code)
        self.assertEqual(numberOfStoredElements, 1)

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