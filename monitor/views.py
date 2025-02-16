from django.shortcuts import render


from .models import Device, NetworkMetric, Alert
import json


def dashboard(request):
    devices = Device.objects.all()
    alerts = Alert.objects.all()

    # Prepare data for Chart.js
    metrics = NetworkMetric.objects.all().order_by("-recorded_at")[
        :10
    ]  # Last 10 entries
    labels = [m.recorded_at.strftime("%H:%M:%S") for m in metrics]
    bandwidth_usage = [m.bandwidth_usage for m in metrics]
    latency = [m.latency for m in metrics]
    packet_loss = [m.packet_loss for m in metrics]

    context = {
        "devices": devices,
        "alerts": alerts,
        "labels": json.dumps(labels),
        "bandwidth_usage": json.dumps(bandwidth_usage),
        "latency": json.dumps(latency),
        "packet_loss": json.dumps(packet_loss),
    }
    return render(request, "dashboard.html", context)
