from django.db import models


class SensorType(models.Model):
    type = models.CharField("Sensor Type", max_length=100, unique=True)
    model = models.CharField("Sensor Model", max_length=100)

    def __str__(self):
        return f"{self.type} - {self.model}"

    class Meta:
        unique_together = ('type', 'model')


class Manufacturer(models.Model):
    name = models.CharField("Manufacturer", max_length=150)

    def __str__(self):
        return f"{self.name}"


class Sensor(models.Model):
    SENSOR_STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Maintenance')
    ]

    sensor_type = models.ForeignKey(SensorType, on_delete=models.SET_NULL, verbose_name="Sensor Type", null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, verbose_name="Manufacturer", null=True, blank=True)
    installation_date = models.DateField("Installation Date")
    status = models.CharField("Status", max_length=20, choices=SENSOR_STATUS_CHOICES)

    def __str__(self):
        return f"{self.sensor_type}"


class Session(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Session from {self.start_time} to {self.end_time} - {getattr(self, 'description', "No description")}"


class DataType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    unit = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.unit})"


class Data(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='data')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='data', verbose_name="Measurement Session")
    data_type = models.ForeignKey(DataType, on_delete=models.CASCADE, verbose_name="Type of Data")
    value = models.FloatField("Value")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at}: {self.data_type.name} = {self.value} {self.data_type.unit}"


class Alert(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='alerts')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert on {self.created_at} for {self.sensor}"
