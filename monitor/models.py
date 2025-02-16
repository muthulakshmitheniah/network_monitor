from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    status = models.CharField(
        max_length=10, choices=[("Online", "Online"), ("Offline", "Offline")]
    )

    def __str__(self):
        return self.name


class NetworkMetric(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    bandwidth_usage = models.FloatField()
    latency = models.FloatField()
    packet_loss = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Metrics for {self.device.name} at {self.recorded_at}"


class Alert(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    severity = models.CharField(
        max_length=10, choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")]
    )
    triggered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert: {self.message} ({self.severity})"
