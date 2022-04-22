import mysql.connector as sql
mycon=sql.connect(host='localhost', user='root', passwd='', database='abc')
    
cursor=mycon.cursor();

name=input("Enter name: ")
comm="select * from student where name='{}'".format(name)
cursor.execute(comm)
data=cursor.fetchall()

for row in data:
    print(row)
    
records = cursor.rowcount
print('Number of records: ', records)   

mycon.close()
