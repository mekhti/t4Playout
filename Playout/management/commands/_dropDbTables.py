from django.db import connection

def dropAllTables():
    cursor = connection.cursor()
    cursor.execute('SHOW TABLES;')
    tablesList = cursor.fetchall()

    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.fetchall()

    for nextTable in tablesList:
        sqlString = 'DROP TABLE IF EXISTS ' + nextTable[0]
        cursor.execute(sqlString)
        cursor.fetchall()
        if()
    return 1
