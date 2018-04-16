from django.shortcuts import render
from apps.home.models import *
from apps.home.serializers import *
from rest_framework import generics
from rest_framework.utils import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class ToolList(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer


class ExampleList(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer



class TutorialList(generics.ListCreateAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

    def get_queryset(self):
        st = super().get_queryset()
        toolId = self.request.GET['toolId']
        st = st.filter(tool_id = toolId)
        return st

    def create(self, request, *args, **kwargs):
        data = json.loads(request.body)
        tool = Tool.objects.get(id=data['tool'])
        data['tool'] = tool
        Tutorial.objects.create(**data)
        return Response(status=status.HTTP_200_OK)
