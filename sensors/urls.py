from django.urls import path

from sensors.views import SensorViewSet, SessionViewSet

urlpatterns = [
    path('sensors/', SensorViewSet.as_view({"get": "list", "post": "create"}), name='sensors-list'),
    path('sensors/<int:pk>/', SensorViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='sensors-detail'),

    path('sessions/', SessionViewSet.as_view({"get": "list", "post": "create"}), name='sessions-list'),
    path('sessions/<int:pk>/', SessionViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='sessions-detail'),
    path('sessions/<int:pk>/add_data/', SessionViewSet.as_view({"post": "add_data"}), name='sessions-add-data'),
]
