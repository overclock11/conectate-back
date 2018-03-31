from rest_framework import serializers
from apps.home.models import Tool

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ('id','name','keyWords','technicalDetails','description')