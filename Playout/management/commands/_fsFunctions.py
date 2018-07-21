import os
import re
import glob
import logging

from Playout.management.commands._funcs import *

BASEPATH = os.path.dirname(os.path.abspath("manage.py"))
PATH_DELIMIMTER = definePathDelimiter()

LOGGER = logging.getLogger('manage')

def findMigrationsFiles(appName):
    LOGGER.info('Getting list of migration files.')
    migrationsFolderPath = BASEPATH + PATH_DELIMIMTER
    migrationsFolderPath += (appName + PATH_DELIMIMTER)
    migrationsFolderPath += ("migrations" + PATH_DELIMIMTER)

    searchPathString = migrationsFolderPath + PATH_DELIMIMTER + '*.py'
    unsortedFilesList = glob.glob(searchPathString)

    filesList = []
    r = re.compile(r'__init__.py', re.I)

    for nextFile in unsortedFilesList:
        if not r.search(nextFile):
            filesList.append(nextFile)

    searchPathString = migrationsFolderPath + PATH_DELIMIMTER + '*.pyc'
    unsortedFilesList = glob.glob(searchPathString)

    for nextFile in unsortedFilesList:
        filesList.append(nextFile)

    LOGGER.info('Found ' + str(len(filesList)) + ' files.')
    return filesList

def clearMigrations(appName):
    LOGGER.info('Preparing clearence of migration files')
    filesToRemoving = findMigrationsFiles(appName)
    for nextFile in filesToRemoving:
        LOGGER.debug('Checking file %s for existing.', nextFile)
        if os.path.exists(nextFile):
            try:
                LOGGER.debug('Deleting file %s.', nextFile)
                os.remove(nextFile)
            except OSError as err:
                LOGGER.error('Can\'t delete file: %s due to system error: {0}'.format(err), (str(nextFile)))

def clearCacheFiles():
    pass



