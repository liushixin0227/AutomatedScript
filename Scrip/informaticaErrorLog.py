import cx_Oracle
import os
import sys
import platform
import cx_Oracle

def version():
    '''Display versions of python, cx_Oracle module
    # and Oracle client being used...'''
    print("Python version: " + platform.python_version())
    print("cx_Oracle version: " + cx_Oracle.version)
    print("Oracle client: " + str(cx_Oracle.clientversion()).replace(', ', '.'))

    print("Oracle DB version: " + conn.version)
    print("Oracle client encoding: " + conn.encoding)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
sqlfp = open('F:\WorkFolder\Script\SQL\InformaticaDevelopErrorLog.sql', 'r', encoding='utf-8')
sql = sqlfp.read()
conn = cx_Oracle.connect('mcsods/McsOds#LvBang#171@MCSDB')

version()
cursor = conn.cursor()
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    for i in range(len(row)):
        print(row[i],end=',')
    print()

cursor.close()
conn.close()
