from django.contrib import admin

from sensors.models import Sensor, SensorType, Manufacturer, Alert, DataType, Data, Session

admin.site.register(Sensor)
admin.site.register(SensorType)
admin.site.register(Manufacturer)
admin.site.register(Alert)
admin.site.register(DataType)
admin.site.register(Data)
admin.site.register(Session)
