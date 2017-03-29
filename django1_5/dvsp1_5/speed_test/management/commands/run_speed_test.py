from django.core.management.base import BaseCommand

from speed_test.action_speed_test import ActionSpeedTest


class Command(BaseCommand):
    help = "Speed Test Django 1.5"

    def handle(self, *args, **options):
        ActionSpeedTest(10000)
