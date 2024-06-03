from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from sensors.models import Sensor, DataType, SensorType
from sensors.serializers import SensorSerializer
from sensors.serializers.sensors import SensorTypeSerializer


class SensorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sensor_type__type', 'manufacturer__name', 'status']

    def get_queryset(self):
        queryset = super().get_queryset()
        sensor_type = self.request.query_params.get('type')
        if sensor_type is not None:
            queryset = queryset.filter(sensor_type__type=sensor_type)
        return queryset


class DataTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = DataType.objects.all()
    serializer_class = DataType


class SensorTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer
