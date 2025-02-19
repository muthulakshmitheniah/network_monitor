from django.db import models


class Network(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ip_address = models.GenericIPAddressField(unique=True)
    status = models.CharField(
        max_length=20, choices=[("Online", "Online"), ("Offline", "Offline")]
    )

    def __str__(self):
        return self.name


class NetworkMetric(models.Model):
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    bandwidth_usage = models.FloatField()
    latency = models.FloatField()
    packet_loss = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.network.name} - {self.recorded_at}"


class Alert(models.Model):
    network = models.ForeignKey(
        Network, on_delete=models.CASCADE, null=True, blank=True
    )
    message = models.TextField()
    severity = models.CharField(
        max_length=10, choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for {self.network.name if self.network else 'Unknown'}: {self.message}"
