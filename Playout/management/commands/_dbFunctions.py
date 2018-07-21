from django.db import connection
import logging

LOGGER = logging.getLogger('manage')

cursor = connection.cursor()

def listTables(logVerbosity = 1):
    LOGGER.info('Preparing tables list.')
    cursor.execute('SHOW TABLES;')
    t = cursor.fetchall()
    tableList = []
    for nextTable in t:
        tableList.append(nextTable[0])

    LOGGER.info('Found %s tables.', str(len(tableList)))
    return tableList

def dropTable(tName):
    if isinstance(tName, list):
        LOGGER.info('List of tables recieved. Preparing dropping operation.')
        LOGGER.debug('Setting FOREIGN_KEY_CHECKS parameter to 0(zero).')
        cursor.execute('SET FOREIGN_KEY_CHECKS=0')
        cursor.fetchone()
        for nextTable in tName:
            LOGGER.info('Dropping %s table from database.', str(nextTable))
            sqlString = 'DROP TABLE IF EXISTS ' + nextTable
            cursor.execute(sqlString)
            cursor.fetchone()
        LOGGER.debug('Setting FOREIGN_KEY_CHECKS parameter back to 1(one).')
        cursor.execute('SET FOREIGN_KEY_CHECKS=1')
        cursor.fetchone()
        return 1
    elif isinstance(tName, str):
        LOGGER.info('Single table name recieved. Preparing dropping operation.')
        LOGGER.debug('Setting FOREIGN_KEY_CHECKS parameter to 0(zero).')
        cursor.execute('SET FOREIGN_KEY_CHECKS=0')
        cursor.fetchone()
        LOGGER.info('Dropping %s table from database.', str(tName))
        sqlString = 'DROP TABLE IF EXISTS ' + tName
        cursor.execute(sqlString)
        cursor.fetchone()
        return 1
    else:
        LOGGER.error('Wrong type of data passed to function. '
                     'Table name must be string or list of strings.')
        return -1

def dropAllTables():
    LOGGER.info('Preparing to delete all tables.')
    tList = listTables()
    dropTable(tList)
    return 1