from django.core.management.base import BaseCommand, CommandError

import logging
import Playout.management.commands._fsFunctions as FSFunctions
import Playout.management.commands._dbFunctions as DBFunctions

logger = logging.getLogger('manage')

class Command(BaseCommand):
    help = """
    Reset all files to default
    """

    def handle(self, *args, **options):
        options['verbosity'] = int(options['verbosity'])
        if options['verbosity'] > 1:
            if options['verbosity'] == 2:
                logger.setLevel(logging.INFO)
            else:
                logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.WARNING)
        logger.info('Preparing clearing all migration artefacts from project folder.')
        FSFunctions.clearMigrations('Playout')
        DBFunctions.dropAllTables()

