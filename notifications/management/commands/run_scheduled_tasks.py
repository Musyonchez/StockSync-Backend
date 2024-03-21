from django.core.management.base import BaseCommand
from ...scheduled_tasks import start_scheduling

class Command(BaseCommand):
    help = 'Runs scheduled tasks.'

    def handle(self, *args, **options):
        start_scheduling()
