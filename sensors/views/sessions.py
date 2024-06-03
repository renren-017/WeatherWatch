from django.core.cache import cache
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from config import settings
from sensors.models import Session
from sensors.serializers import SessionSerializer, DataCreateSerializer


class SessionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Session.objects.all().prefetch_related('data')
    serializer_class = SessionSerializer

    def get_serializer_class(self):
        if self.action == 'add_data':
            return DataCreateSerializer
        return SessionSerializer

    @action(detail=True, methods=['post'], serializer_class=DataCreateSerializer)
    def add_data(self, request, pk=None):
        session = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(session=session)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        cache_key = "sensors_" + "_".join(list(self.request.query_params.values()))
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(data=cached_data, status=status.HTTP_200_OK)
        result = super().list(request, *args, **kwargs)
        cache.set(cache_key, result.data, settings.DEFAULT_CACHE_TIMEOUT)
        return result

    def perform_create(self, serializer):
        serializer.save()
