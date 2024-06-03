from rest_framework import viewsets
from sensors.models import Alert
from sensors.serializers import AlertSerializer, AlertCreateSerializer


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all().order_by('-id')
    serializer_class = AlertSerializer

    def get_serializer_class(self):
        if self.action in ('create', 'put'):
            return AlertCreateSerializer
        return AlertSerializer
