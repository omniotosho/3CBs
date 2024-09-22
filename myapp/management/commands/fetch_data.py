from django.core.management.base import BaseCommand
from myapp.fetch_data import fetch_and_store_data

class Command(BaseCommand):
    help = 'Fetches data from external API and stores in database'

    def handle(self, *args, **kwargs):
        fetch_and_store_data()
        self.stdout.write(self.style.SUCCESS('Data fetched and stored successfully'))
