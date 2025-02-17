from django.urls import path
from .views import network_list, network_dashboard

urlpatterns = [
    path("networks/", network_list, name="network_list"),
    path("dashboard/", network_dashboard, name="network_dashboard"),
]
