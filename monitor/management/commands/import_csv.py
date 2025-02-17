import csv
import os
from django.core.management.base import BaseCommand
from monitor.models import Network, NetworkMetric, Alert
from django.utils import timezone


class Command(BaseCommand):
    help = "Import network data from a CSV file"

    def handle(self, *args, **kwargs):
        csv_file_path = os.path.join(
            "monitor", "data", "network_data.csv"
        )  # Ensure correct path

        if not os.path.exists(csv_file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {csv_file_path}"))
            return

        with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                network, created = Network.objects.get_or_create(
                    name=row["network_name"],
                    ip_address=row["ip_address"],
                    defaults={"status": row["status"]},
                )

                NetworkMetric.objects.create(
                    network=network,
                    bandwidth_usage=float(row["bandwidth_usage"]),
                    latency=float(row["latency"]),
                    packet_loss=float(row["packet_loss"]),
                    recorded_at=timezone.now(),
                )

                if row["alert_message"]:
                    Alert.objects.create(
                        network=network,
                        message=row["alert_message"],
                        severity=row["alert_severity"],
                        created_at=timezone.now(),
                    )

        self.stdout.write(self.style.SUCCESS("CSV data imported successfully."))
