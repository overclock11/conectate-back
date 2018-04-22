from django.shortcuts import render
from apps.home.models import *
from apps.home.serializers import *
from rest_framework import generics
from rest_framework.utils import json
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class ToolList(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

    @detail_route()
    def tutorials(self, request, pk=None):
        tool = Tool.objects.get(id=pk)
        tutorials = TutorialSerializer(tool.tutorials, many=True)
        return Response(tutorials.data)


    @detail_route()
    def examples(self, request, pk=None):
        tool = Tool.objects.get(id=pk)
        examples = ExampleSerializer(tool.examples, many=True)
        return Response(examples.data)


class ExampleList(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer


class TutorialList(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

class ResourceList(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class PedagogicStrategyList(viewsets.ModelViewSet):
    queryset = PedagogicStrategy.objects.all()
    serializer_class = PedagogicStrategySerializer

class DisciplineList(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer