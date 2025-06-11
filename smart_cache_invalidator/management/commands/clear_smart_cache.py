from django.core.management.base import BaseCommand
from smart_cache_invalidator.utils import clear_smart_cache

class Command(BaseCommand):
    help = 'Clears the smart cache'

    def handle(self, *args, **kwargs):
        clear_smart_cache()
        self.stdout.write(self.style.SUCCESS('Successfully cleared the smart cache'))