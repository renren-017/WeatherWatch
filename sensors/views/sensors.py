import os

from django.views.decorators.cache import cache_page
from rest_framework import viewsets, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from config import settings
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

    def list(self, request, *args, **kwargs):
        cache_key = "sensors_" + "_".join(list(self.request.query_params.values()))
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(data=cached_data, status=status.HTTP_200_OK)
        result = super().list(request, *args, **kwargs)
        cache.set(cache_key, result.data, settings.DEFAULT_CACHE_TIMEOUT)
        return result


class DataTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = DataType.objects.all()
    serializer_class = DataType


class SensorTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer
