from rest_framework import serializers
from apps.home.models import *

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = '__all__'


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'


class PedagogicStrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = PedagogicStrategy
        fields = '__all__'

class ExampleSerializer(serializers.ModelSerializer):
    discipline = DisciplineSerializer(many=False, read_only=True)
    pedagogic_strategy = PedagogicStrategySerializer(many=False, read_only=True)
    class Meta:
        model = Example
        fields = '__all__'
