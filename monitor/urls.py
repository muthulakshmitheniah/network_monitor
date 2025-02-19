from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    network_list,
    network_dashboard,
    dashboard_view,
    alert_view,
    add_network_data,
    register,
)

urlpatterns = [
    path("networks/", network_list, name="network_list"),
    path("dashboard/", network_dashboard, name="network_dashboard"),
    path("", dashboard_view, name="dashboard"),
    path("alerts/", alert_view, name="alerts"),
    path("network/add/", add_network_data, name="add_network_data"),
    path("register/", register, name="register"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
]
