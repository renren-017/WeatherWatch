from rest_framework import serializers
from sensors.models import Session, Data, Sensor, DataType

from sensors.serializers.sensors import SensorSerializer

__all__ = ['SessionSerializer', 'DataCreateSerializer']


class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = ['name', 'unit']


class DataSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer(read_only=True)
    data_type = DataTypeSerializer(read_only=True)

    class Meta:
        model = Data
        fields = ['sensor', 'data_type', 'value', 'created_at']
        read_only_fields = ['created_at']


class DataCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['sensor', 'data_type', 'value', 'created_at']
        read_only_fields = ['created_at']


class SessionSerializer(serializers.ModelSerializer):
    data = DataSerializer(many=True, read_only=True)

    class Meta:
        model = Session
        fields = ['id', 'start_time', 'end_time', 'description', 'data']
