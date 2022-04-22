# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 08:38:30 2020

@author: DELL
"""
import pymysql as sql
mycon=sql.connect('localhost', 'root', '', 'abc')
    
cursor=mycon.cursor();
cursor.execute('delete from student where name="Aditya"')
cursor.execute("select * from student")
data=cursor.fetchall()

for row in data:
    print(row)
    
records = cursor.rowcount
print('Number of records: ', records)   

mycon.close()
