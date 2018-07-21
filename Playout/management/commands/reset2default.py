from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = """
    Reset all files to default
    """

    def handle(self, *args, **options):
        pass