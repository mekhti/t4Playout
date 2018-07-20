from django.core.management.base import BaseCommand, CommandError
from Playout.management.commands._funcs import *

class Command(BaseCommand):
    help = 'Dump active databases to sql file'

    def handle(self, *args, **options):
        pass