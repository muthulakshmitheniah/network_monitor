# Register your models here.
from django.contrib import admin
from .models import Network, NetworkMetric, Alert

admin.site.register(Network)
admin.site.register(NetworkMetric)
admin.site.register(Alert)
