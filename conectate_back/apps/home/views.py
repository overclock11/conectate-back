from django.shortcuts import render
from apps.home.models import *
from apps.home.serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.

class ToolListAll(APIView):
    def get_object(self):
        try:
            return Tool.objects.all()
        except Tool.DoesNotExist:
            raise Http404

    def get(self):
        tools = Tool.objects.all()
        return Response(serializer.data)


# class SuperHeroesList(APIView):
#     def get_object(self, superheroe_name):
#         try:
#             return SuperHeroes.objects.get(name=superheroe_name)
#         except SuperHeroes.DoesNotExist:
#             raise Http404
#
#     def get(self, request, superheroe_name, format=None):
#         heroe = self.get_object(superheroe_name)
#         serializer = SuperHeroesSerializer(heroe)
#         return Response(serializer.data)
#
#     def put(self, request, superheroe_name, format=None):
#         heroe = self.get_object(superheroe_name)
#         serializer = SuperHeroesSerializer(heroe, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, superheroe_name, format=None):
#         heroe = self.get_object(superheroe_name)
#         heroe.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)