from django import forms
from .models import Network, NetworkMetric, Alert


class NetworkForm(forms.ModelForm):
    class Meta:
        model = Network
        fields = ["name", "ip_address", "status"]


class NetworkMetricForm(forms.ModelForm):
    class Meta:
        model = NetworkMetric
        fields = ["network", "bandwidth_usage", "latency", "packet_loss"]


class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ["network", "message", "severity"]
