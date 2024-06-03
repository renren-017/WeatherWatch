from rest_framework import serializers
from sensors.models import Alert

from sensors.serializers.sensors import SensorSerializer

__all__ = [
    'AlertCreateSerializer', 'AlertSerializer'
]


class AlertSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer(read_only=True)

    class Meta:
        model = Alert
        fields = ['sensor', 'description', 'created_at']


class AlertCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['sensor', 'description', 'created_at']
        read_only_fields = ['created_at']
