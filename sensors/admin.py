from django.contrib import admin
from sensors.models import SensorType, Manufacturer, Sensor, Session, DataType, Data, Alert


@admin.register(SensorType)
class SensorTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'model')
    list_filter = ('type', 'model')
    ordering = ('type', 'model')
    search_fields = ('type', 'model')


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_type', 'manufacturer', 'installation_date', 'status')
    list_filter = ('sensor_type', 'manufacturer', 'status')
    ordering = ('installation_date', 'sensor_type')
    search_fields = ('sensor_type__type', 'manufacturer__name', 'status')


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'description')
    list_filter = ('start_time', 'end_time')
    ordering = ('start_time', 'end_time')
    search_fields = ('description',)


@admin.register(DataType)
class DataTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name', 'unit')


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'session', 'data_type', 'value', 'created_at')
    list_filter = ('sensor', 'session', 'data_type', 'created_at')
    ordering = ('created_at', 'sensor')
    search_fields = ('sensor__sensor_type__type', 'data_type__name', 'value')


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'description', 'created_at')
    list_filter = ('sensor', 'created_at')
    ordering = ('created_at', 'sensor')
    search_fields = ('description', 'sensor__sensor_type__type')
