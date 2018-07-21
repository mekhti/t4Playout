from django.db import connection

cursor = connection.cursor()

def listTables():
    cursor.execute('SHOW TABLES;')
    t = cursor.fetchall()
    tableList = []
    for nextTable in t:
        tableList.append(nextTable[0])
    return tableList

def dropTable(tName):
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.fetchone()
    sqlString = 'DROP TABLE IF EXISTS ' + tName
    cursor.execute(sqlString)
    cursor.fetchone()
    return 1

def dropAllTables():
    tList = listTables()
    for nextTable in tList:
        dropTable(nextTable)
    return 1