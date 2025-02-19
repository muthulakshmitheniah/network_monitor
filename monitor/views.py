from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Network, NetworkMetric, Alert
import os
import pandas as pd
from .forms import NetworkForm, NetworkMetricForm, AlertForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .decorators import group_required


@group_required("Admin", "User")
def network_list(request):
    """View to display all networks."""
    networks = Network.objects.all()
    return render(request, "network_list.html", {"networks": networks})


@group_required("Admin", "User")
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


@group_required("Admin", "User")
def dashboard_view(request):
    return render(request, "dashboard.html")


def get_alerts(network=None):
    """Fetch the latest alerts. If a specific network is provided, filter by that network."""
    if network:
        return Alert.objects.filter(network=network).order_by("-created_at")[
            :5
        ]  # Latest 5 alerts for specific network
    return Alert.objects.order_by("-created_at")[:5]  # Latest 5 alerts for all networks


def alert_view(request):
    """View to render alerts separately."""
    alerts = get_alerts()
    return render(request, "alert.html", {"alerts": alerts})


@group_required("Admin")
def add_network_data(request, network_id=None):
    network = None
    if network_id:
        network = Network.objects.get(id=network_id)  # Fetch the selected network

    if request.method == "POST":
        network_form = NetworkForm(request.POST)
        metric_form = NetworkMetricForm(request.POST)
        alert_form = AlertForm(request.POST)

        if network_form.is_valid() and metric_form.is_valid() and alert_form.is_valid():
            if not network:
                network = network_form.save()  # Create new network if not provided

            metric = metric_form.save(commit=False)
            metric.network = network  # Auto-assign the network
            metric.save()

            if alert_form.cleaned_data.get("message") and alert_form.cleaned_data.get(
                "severity"
            ):
                alert = alert_form.save(commit=False)
                alert.network = network  # Auto-assign the network
                alert.save()

            return redirect("network_list")  # Redirect to a list view
    else:
        network_form = NetworkForm(instance=network) if network else NetworkForm()
        metric_form = NetworkMetricForm()
        alert_form = AlertForm()

    return render(
        request,
        "add_network_data.html",
        {
            "network_form": network_form,
            "metric_form": metric_form,
            "alert_form": alert_form,
            "network": network,
        },
    )


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})
