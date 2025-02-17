from django.shortcuts import render
from .models import Network, NetworkMetric


def network_list(request):
    """View to display all networks."""
    networks = Network.objects.all()
    return render(request, "network_list.html", {"networks": networks})


def network_dashboard(request):
    all_networks = Network.objects.all()
    selected_network_name = request.GET.get("network", None)
    selected_network = None
    labels, bandwidth_usage, latency, packet_loss = [], [], [], []

    if selected_network_name:
        selected_network = Network.objects.filter(name=selected_network_name).first()
        if selected_network:
            metrics = NetworkMetric.objects.filter(network=selected_network).order_by(
                "recorded_at"
            )

            labels = [metric.recorded_at.strftime("%H:%M:%S") for metric in metrics]
            bandwidth_usage = [metric.bandwidth_usage for metric in metrics]
            latency = [metric.latency for metric in metrics]
            packet_loss = [metric.packet_loss for metric in metrics]

    return render(
        request,
        "network_dashboard.html",
        {
            "all_networks": all_networks,
            "selected_network": selected_network,
            "labels": labels,
            "bandwidth_usage": bandwidth_usage,
            "latency": latency,
            "packet_loss": packet_loss,
        },
    )
