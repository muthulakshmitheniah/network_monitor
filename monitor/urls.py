from django.urls import path
from .views import network_list, network_dashboard, dashboard_view, alert_view

urlpatterns = [
    path("networks/", network_list, name="network_list"),
    path("dashboard/", network_dashboard, name="network_dashboard"),
    path("", dashboard_view, name="dashboard"),
    path("alerts/", alert_view, name="alerts"),
]
