from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

    def perform_create(self, serializer):
        serializer.save()
