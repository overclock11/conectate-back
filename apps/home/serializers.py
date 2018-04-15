from rest_framework import serializers
from apps.home.models import Tool, Tutorial, Example

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ('id','name','keyWords','technicalDetails','description')


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id', 'name', 'url', 'commentary', 'tool')


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = '__all__'