# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:27:14 2021

@author: hp
"""
'''
Q1. Bubble sort
'''
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
             if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
arr = [64, 34, 25, 12, 22, 11, 90] 
bubbleSort(arr) 
print(arr)


'''
Q2. Class pickle demo
'''
import pickle
class student:
    
    def __init__(self,mroll=0,mname =' ',mmark1 = 0):
        self.roll = mroll
        self.name = mname
        self.mark1 = mmark1
        
    def readmarks(self):
        self.roll = int(input('enter roll number  '))
        self.name = input('enter name of the student ')
        self.mark1 = int(input('enter marks '))
		 
    def display(self):
        print(self.roll,self.name,self.mark1)
	 
'''
ofile = open('xiib.txt','ab')

stud1 = student(0, '',0)

for i in range(1):
    stud1.readmarks()
    pickle.dump(stud1,ofile)

ofile.close()

'''

stud1 = student()

ifile = open('xiib.txt','rb')
try:
    while True:
        stud1 = pickle.load(ifile)
        stud1.display()
except EOFError:
    ifile.close()
 

 
'''
Q3. CSV file
'''
import pandas as pd
import numpy as np

df = pd.read_csv('ELECTRICITY.CSV', names =['NAME','CURRENT_READ','PREVIOUS_READ'])

df['Consumed'] = df['CURRENT_READ']-df['PREVIOUS_READ']
print(df)

 
'''
Q4. File handling
'''
def data_entry():
    
    ofile = open('xiib.dat', 'w')
    for i in range (1,4):
        name = input('Enter Name : ')
        age  = input('Enter Age  : ')
        record = name+'#'+age+'\n'
        ofile.write(record)
    ofile.close()


def display_output():
    infile = open('xiib.dat', 'r')
    for i in range (1,4):
        record = infile.readline()
        data = record.split('#')
        print(data[0], data[1].rstrip('\n') )
    infile.close()

#data_entry()
display_output()

'''
Q6. Use of CSV file
'''
import csv
from colorama import Fore, Back, Style 
print(Fore.RED + 'Stuti')

def data_entry():
    with open('petrol_pump.csv', 'w') as ofile:
         writer = csv.writer(ofile, delimiter = ',')
	
         
         choice ='y'
         while choice =='y':
             date = input('enter today\'s date: ')
             sno =  int(input('Enter S.No.  :'))
             vno =  input('Enter Vehicle Number :')
             
             rec = [date,sno,vno]
             writer.writerow(rec)
             choice = input('do you want to continue ?')
    ofile.close()
    


def display_data():
    with open('petrol_pump.csv','r') as infile:
        data = csv.reader(infile)
        print('\n\n\n')
        print(Fore.RED+'\t Bhumika Petrol Pump Bhilai\n')
        print(Fore.BLACK)
        for row in data:  
            if row!=[]:
                print(row[0],'  ', row[1],' ',row[2])
    infile.close()
    
#data_entry()
display_data()

'''
Q7. Petrol pump project
'''
import csv

def data_entry():
    with open('stuti_petrol_pump.csv' , 'a') as infile:
        writer=csv.writer(infile,delimiter=',')

        choice='y'
        while choice=='y':
            date=input('enter today\'s date: ')
            sno=int(input('enter S.No.  :'))
            vno=input('enter vehicle number:')
            oil=input('enter oil type:')
            litres=int(input('enter no. of litres:'))
            amount=int(input('enter amount:'))
            paymode=input('enter paymode card/cash/paytm:')

            rec=[date,sno,vno,oil,litres,amount,paymode]
            writer.writerow(rec)
            choice=input('do you want to continue y/n :')

        infile.close()    

 
def display_data():
    with open('stuti_petrol_pump.csv','r')as infile:
        data=csv.reader(infile)
        print('\n\n\n')
        print('\t Trivedi Petrol Pump Bhilai\n')
        for row in data:
            if row!=[]:
                print(row[0],'  ',row[1],'  ',row[2],'  ',row[3],'  ',row[4],'  ',row[5])
    infile.close()
                      
    
choice =0

while choice !=3:
    
    print('\n\n\n\n') 
    print('Main Menu')
    print('*******************')
    print('1. Data entry')
    print('2. View Data ')    
    print('3. Quit ')    
    choice = int(input('Enter your choice : '))
    if choice ==1:
        data_entry()
        ch = input('Press Enter key to continue....')
        
    elif choice ==2:
        display_data()
        ch = input('Press a Enter key to continue....')
        
    elif choice ==3:
        print('Made by Stuti....the Genius!!!')
        break



'''
Q8. Using Pymysql
'''
import pymysql as pym
mycon = pym.connect('localhost','root','dpsb','dps')

cursor = mycon.cursor()
cursor.execute('select * from student')
data = cursor.fetchall()
count = cursor.rowcount
for row in data:
	print(row)

print('Total number of records:',count)
mycon.close()

'''
Q9. Selection sort
'''
A = [64, 25, 12, 22, 11] 
  
 
for i in range(len(A)): 
    
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)):
        
        if A[min_idx] > A[j]:
            
            min_idx = j 
              
    A[i], A[min_idx] = A[min_idx], A[i] 
   
print ("Sorted array") 
print(A)

'''
Q10. Bubble sort
'''
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
             if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
arr = [64, 34, 25, 12, 22, 11, 90] 
bubbleSort(arr) 
print(arr)

'''
Q11. CSV file
'''
import csv

def Data_entry():
    
    info = [['SNO', 'Person', 'DOB'], \
    ['1', 'Madhu', '18/12/2001'],\
    ['2', 'Sowmya','19/2/1998'], \
    ['3', 'Sangeetha','20/3/1999'], \
    ['4', 'Eshwar', '21/4/2000'],\
    ['5', 'Anand', '22/5/2001']]

    

    with open('person.csv', 'w') as f:

        writer = csv.writer(f, delimiter = ',')

        for row in info:

            writer.writerow(row)

        f.close()
        

def Display_data():
    import csv
    with open('person.csv','rt') as f:
        data = csv.reader(f)  
        for row in data:
            if row!=[]:
                print(row[0],'  ', row[1],'  ',row[2])


#Data_entry()
Display_data()

'''
Q12. PyMYSQL demo
'''
import pymysql as pym
mycon = pym.connect('localhost','root','dpsb','dps')

cursor = mycon.cursor()
cursor.execute('select * from student')
data = cursor.fetchall()
count = cursor.rowcount
for row in data:
	print(row)

print('Total number of records:',count)
mycon.close()

'''
Q13. STACK  Push and POP
'''
def isEmpty(stack):
	if len(stack)==0:
		return True
	else:
		return False

def Push(stack,item):
	stack.append(item)
	top = len(stack)-1


def Pop(stack):
	if isEmpty(stack):
		return 'Underflow'
	else:
		item = stack.pop()
		if len(stack)==0:
			top = None
		else:
			top = len(stack)-1
	return item

def Peek(stack):
	if isEmpty(stack):
		return 'Underflow'
	else:
		top = len(stack)-1
		return stack[top]

def Display(stack):
	if isEmpty(stack):
		print('Stack is empty')
	else:
		top = len(stack)-1
		for a in range(top-1, -1,-1):
			print(stack[top])
'''
Q14. Queue insert and delete
'''
def  isempty(que):
	if que==[]:
		return True
	else:
		return False


def enqueue(Que,item):
	que.append(item)
	if len(que)==1:
		front = rear = 0
	else:
		rear = len(que)+1
	print(item, 'inserted successfully')


def dequeue(que):
	if isempty(que):
		return 'Underflow'
	else:
		item = que.pop(0)
	if len(que)==0:
		front = rear = None
	return item


def  peek(que):
	if isempty(que):
		return 'Queue is empty'
	else:
		return que[0]



def display_queue(que):
	if isempty(que):
		print('Queue is empty')
	else:
        if len(que)==1:
            print(que[0])
	    else:
		    for i in range(front,rear):
			    print(que[i])


                                 ---ZUNJANI---