# Register your models here.
from django.contrib import admin
from .models import Device, NetworkMetric, Alert

# Register models to appear in admin panel
admin.site.register(Device)
admin.site.register(NetworkMetric)
admin.site.register(Alert)
