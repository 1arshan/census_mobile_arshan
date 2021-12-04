# from django.db import models
from rest_framework import serializers
from census.models import State,District,Child,File

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model= State
        fields= '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model=District
        fields= '__all__'

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model=Child
        fields='__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model=File
        fields="__all__"