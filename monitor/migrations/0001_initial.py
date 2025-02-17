# Generated by Django 5.1.6 on 2025-02-16 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('ip_address', models.GenericIPAddressField(unique=True)),
                ('status', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('severity', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('network', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.network')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bandwidth_usage', models.FloatField()),
                ('latency', models.FloatField()),
                ('packet_loss', models.FloatField()),
                ('recorded_at', models.DateTimeField(auto_now_add=True)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.network')),
            ],
        ),
    ]
