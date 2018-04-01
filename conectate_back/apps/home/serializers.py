from rest_framework import serializers
from apps.home.models import Tool, Tutorial

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ('id','name','keyWords','technicalDetails','description')

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id', 'name', 'url', 'commentary', 'tool')