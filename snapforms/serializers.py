from rest_framework import serializers
from .models import LocationRequest

class LocationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationRequest
        fields = '__all__'
