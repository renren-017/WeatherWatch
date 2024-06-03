from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from sensors.models import Sensor
from sensors.serializers import SensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sensor_type__type', 'manufacturer__name', 'status']  # Basic filtering

    def get_queryset(self):
        """
        Optionally restricts the returned sensors to a given type,
        by filtering against a `type` query parameter in the URL.
        """
        queryset = super().get_queryset()
        sensor_type = self.request.query_params.get('type')
        if sensor_type is not None:
            queryset = queryset.filter(sensor_type__type=sensor_type)
        return queryset
