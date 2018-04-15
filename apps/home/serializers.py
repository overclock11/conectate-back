from rest_framework import serializers
from apps.home.models import Tool, Tutorial

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id', 'name', 'url', 'commentary', 'tool')