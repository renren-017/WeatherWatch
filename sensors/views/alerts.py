from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from sensors.models import Alert
from sensors.serializers import AlertSerializer, AlertCreateSerializer


class AlertViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Alert.objects.all().order_by('-id')
    serializer_class = AlertSerializer

    def get_serializer_class(self):
        if self.action in ('create', 'put'):
            return AlertCreateSerializer
        return AlertSerializer
