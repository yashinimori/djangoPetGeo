from rest_framework import serializers
from .models import Projects, GeoPoint, GeoLine, GeoPoly


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class GeoPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoPoint
        fields = '__all__'


class GeoLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoLine
        fields = '__all__'


class GeoPolySerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoPoly
        fields = '__all__'
