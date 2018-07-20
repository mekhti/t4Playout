from django.core.management.base import BaseCommand, CommandError
import platform
import os
import glob
from Playout.management.commands._funcs import *
from Playout.management.commands._dropDbTables import *

class Command(BaseCommand):
    help = 'Clean all project to default state'

    def handle(self, *args, **options):
        pathDelimiter = definePathDelimiter()
        basePath = os.path.dirname(os.path.abspath("manage.py"))
        migrationsPath = basePath + pathDelimiter + "Playout" + pathDelimiter + "migrations" + pathDelimiter
        #basePath = os.path.abspath("manage.py")
        print(migrationsPath)

        searchPathString = migrationsPath + pathDelimiter + '*.py'
        unsortedFilesList = glob.glob(searchPathString)
        print(unsortedFilesList)

        print(dropAllTables())
