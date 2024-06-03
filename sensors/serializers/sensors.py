from rest_framework import serializers
from sensors.models import SensorType, Manufacturer, Sensor

__all__ = [
    'SensorSerializer'
]


class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = ['type', 'model']


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name']


class SensorSerializer(serializers.ModelSerializer):
    sensor_type = SensorTypeSerializer(read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'sensor_type', 'manufacturer', 'installation_date', 'status']
