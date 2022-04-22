'''Q-1
Program that copies a text file "source.txt" onto "target.txt" barring the 
lines starting with a '@' sign

'''
file1=open('source.txt',"r")
file2=open('target.txt',"w")
data=file1.readlines()

for line in data:
    if line[0]!="@":
        file2.write(line)

print("Task completed successfully.")
file1.close()
file2.close()

'''Q-2
Program to store empid, name and salary of any 5 emloyees in a file 
'salary.dat' then increase the salary of an employee by 15% whose empid is 101.
After updating a record, print the salary record in a suitable format.

'''
def input_data():
    # to store records in datafile
    file=open('salary.dat',"a")
    for i in range(5):
        empid=int(input("Enter employee ID: "))
        name=input("Enter name of the Employee: ")
        salary=int(input("Enter salary of the Employee: "))
        record=str(empid)+"#"+name+"#"+str(salary)+"\n"
        file.write(record)
        print("Record stored successfully.")
        file.flush()
    file.close()

def update_record():
    # to update a record with enmpid as 101
    import os
    file1=open('salary.dat',"r")
    file2=open('new_salary.dat',"w")
    data=file1.readlines()

    for line in data:
        record=line.rstrip("\n").split("#")
        if record[0]=='101':
            new_salary=int(record[2])*(1+0.15)  #to increase salary by 15%
            record[2]=str(new_salary)
        
        file2.write("#".join(record)+"\n")
        file2.flush()
    
    file1.close()
    file2.close()
    os.remove("salary.dat")
    os.renames("new_salary.dat", "salary.dat")

def print_record():
    # to print salary report
    file=open("salary.dat","r")
    data=file.readlines()

    print("-"*37)
    print("| {:^6s} | {:^15s} | {:^6s} |".format("Emp_ID","Emp_Name","Salary"))
    print("-"*37)
    for line in data:
        record=line.rstrip("\n").split("#")
        print("| {:>6s} | {:<15s} | {:>6s} |".format(record[0], record[1], 
                                                      record[2]))
        print("-"*37)
    file.close()
    
input_data()
update_record()
print_record()

'''Q-3
Program to take a sample text file “words.txt” which has few words then find 
the most commonly occurring word in the text file.

'''
file=open('words.txt',"r")
data=file.read()
max_word=''
count1,count2=0,0
words=[] # list of all words

for line in data.rstrip("\n").split("\n"):
    for word in line.split():
        words.append(word.rstrip(".").lower())
    
for word in words:
    count2=words.count(word)
    if count2>count1:
        count1=count2
        max_word=word
print("'"+max_word+"'","appears maximum times, i.e.,",count1," times")


'''Q-4
Program to create a “inventory.csv” file to store item_name, quantity and 
unit_price of any 5 items then read a file and print the output
'''
import csv
def create_datafile():
#   to create datafile
    file=open('inventory.csv',"a")
    item_name=input("Enter item name: ")
    quantity=int(input("Enter Quantity: "))
    unit_price=int(input("Enter unit price: "))
    record=[item_name,quantity,unit_price]
    writer=csv.writer(file, delimiter=",")
    writer.writerow(record)
    file.flush()
    file.close()
        
def display_report():
    # to display report
    file=open("inventory.csv","r")
    data=csv.reader(file)
    print("{:^50s}".format("Inventory Report"))
    print("-"*50)
    print("| {:^11s} | {:^8s} | {:^10s} | {:^8s} |".format(
        'ITEM NAME', 'QUANTITY', 'UNIT PRICE', 'AMOUNT'))
    print("-"*50)
    for rec in data:
        if rec!=[]:
            print("| {:<11s} | {:>8s} | {:>10s} | {:>8d} |".
                  format(rec[0], rec[1], rec[2], int(rec[1])*int(rec[2])))
            print("-"*50)
    file.close()

for i in range(5):
    create_datafile()
display_report()

'''Q-5
Program to store name, house and mobile number of any five students using 
delimiter ‘@’ in a file ‘student.dat’ and create a file ‘student.txt’ and 
copy all data using delimiter ‘#’.
'''
def input_data():
    # to store data in 'student.dat'
    file=open('student.dat',"a")
    name=input("Enter Name of student: ")
    house=input("Enter house of the student: ")
    mob_no=input("Enter mobile number: ")
    record=name+"@"+house+"@"+mob_no+"\n"
    file.write(record)
    print("Record stored successfully.")
    file.close()
        
def copy_data():
    # to copy data to 'student.txt'
    file1=open("student.dat","r")
    file2=open("student.txt","w")
    data=file1.readlines()
    for record in data:
        lst=record.split("@")
        file2.write('#'.join(lst))
    
    print("Data copied successfully.")
    file1.close()
    file2.close()

for i in range(5):
    input_data()
copy_data()
    

'''Q-6
Program which accepts a hyphen-separated sequence of words as input and prints 
the words in a hyphen-separated sequence after sorting them alphabetically.
'''
def sort_order():
    # to display sequence sorted alphabetically
    seq=input("Enter a hyphen-seperated sequence of words: ")
    lst=seq.split("-")
    lst.sort()
    new_seq='-'.join(lst)
    print(new_seq)
sort_order()


'''Q-7
Program for function that takes amount in dollars and does dollar-to-rupee 
conversion print it then returns the amount converted to rupees.
'''
DOLLER_TO_RUPEES = 73.32
    
def dollar_nonvoid(amount):
    '''
    Parameters
    ----------
    amount : NUMERIC
        amount in dollers.

    Returns
    -------
    amount in Rupees.

    '''
    return int(amount*DOLLER_TO_RUPEES)

def dollar_void(amount):
    '''
    Parameters
    ----------
    amount : NUMERIC
        amount in dollers.

    Returns
    -------
    None.

    '''
    print("Rs",int(amount*DOLLER_TO_RUPEES))

amt=int(input("Enter: "))
print("Non-void:-")
print(dollar_nonvoid(amt))
print("Void:-")
print(dollar_void(amt))


'''Q-8
a module lengthconversion.py that stores functions for various length 
conversion.
'''
MILE_TO_KILOMETER=1.909344
FEET_TO_INCH=12

def miletokm(length):
    '''
    To convert miles into kilometers.

    Parameters
    ----------
    length : NUMERIC
        length in miles.

    Returns
    -------
    length in kilometers.

    '''
    return length*MILE_TO_KILOMETER

def kmtomile(length):
    '''
    To convert kilometers to miles.

    Parameters
    ----------
    length : NUMERIC
        length in kilometrs.

    Returns
    -------
    length in miles.

    '''
    return length/MILE_TO_KILOMETER

def feettoinch(length):
    '''
    To convert  feet into inches.

    Parameters
    ----------
    length : NUMERIC
        length in feet.

    Returns
    -------
    length in inches.

    '''
    return length*FEET_TO_INCH

def inchtofeet(length):
    '''
    To convert inches to feet.

    Parameters
    ----------
    length : NUMMERIC
        length in inches.

    Returns
    -------
    length in feet.

    '''
    return length/FEET_TO_INCH


'''Q-9
Program to create a module massconversion.py that stores functions for various 
mass conversion.
'''
TONNE_TO_KG = 1000
KG_TO_POUND = 2.20462

def kgtotonne(mass):
    '''
    To convert kilograms to tonnes.

    Parameters
    ----------
    mass : NUMERIC
        mass in kilograms.

    Returns
    -------
    mass in tonnes.

    '''
    return mass/TONNE_TO_KG

def tonnetokg(mass):
    '''
    To convert tonne to kilograms.

    Parameters
    ----------
    mass : NUMERIC
        mass in tonnes.

    Returns
    -------
    mass in kilograms.

    '''
    return mass*TONNE_TO_KG

def kgtopound(mass):
    '''
    To convert kilograms to pounds.

    Parameters
    ----------
    mass : NUMERIC
        mass in kilograms.

    Returns
    -------
    mass in pounds.

    '''
    return mass*KG_TO_POUND

def poundtokg(mass):
    '''
    To convert pounds to kilograms.

    Parameters
    ----------
    mass : NUMERIC
        mass in pounds.

    Returns
    -------
    mass in kilograms.

    '''
    return mass/KG_TO_POUND


'''Q-10
Program to store few sentences in a file SENT.TXT then count and print number 
of “to” and “the” present in a file.
'''
#to add sentances
file=open("sent.txt","w")
while True:
    sentance=input("Enter any sentance: ")
    file.write(sentance+"\n")
    file.flush()
    ans=input("Do you want to continue adding sentances([y]/n): ")
    if ans=="n":
        file.close()
        break

#to count number of 'to' & 'the'
file=open("sent.txt","r")
data=file.readlines()
count1,count2=0,0

for line in data:
    rec=line.split()
    for word in rec:
        if word.lower()=="the":
            count1+=1
        elif word.lower()=="to":
            count2+=1

print("Word 'the' appears",count1,"times.")
print("Word 'to' appears",count2,"times.")
file.close()


'''Q-11
Program to create a data file STD.TXT which will store name and phone numbers 
of 5 students and then ask the user to enter name and print his/her phone 
number if it is available in the file otherwise display a message “Not found 
in the directory”.
'''
#to store 5 records
file=open("std.txt",'w')
for i in range(5):
    print("For Student",i+1,":-")
    name=input("Enter name of the Student: ")
    phone=input("Enter student's Mobile no.: ")
    record=name+"#"+phone+"\n"
    file.write(record)
    file.flush()
    print("*"*50)
print("-"*100)
file.close()

#to check for a student
file=open("std.txt","r")
name=input("Enter name of the student you want to search: ")
data=file.readlines()
for line in data:
    record=line.rstrip("\n").split("#")
    if record[0]==name:
        print(name+"'s number is",record[1])
        break
else:
    print("Not found in the directory.")

file.close()


'''Q-12
Program to accept employee’s name and his basic salary of any five employees 
and store in a file EMP.TXT and print the given output.
'''
#to store 5 records
file=open('emp.txt',"w")
for i in range(5):
    print("For Employee",i+1,":-")
    emp_name=input("Enter name of the Employee: ")
    basic=input("Enter his/her Basic salary: ")
    record=emp_name+"#"+basic+"\n"
    file.write(record)
    file.flush()
    print("*"*50)
file.close()
print("-"*100)

#to display salary report
file=open('emp.txt',"r")
data=file.readlines()
print("\n{:^68s}".format("SALARY REGISTER"))
print("-"*68)
print(" {:^5s} {:^25s} {:^6s} {:^6s} {:^6s} {:^6s} {:^6s}".
      format("S.No.","Name","Basic","DA","HRA","Total","PF"))

print("-"*68)

s_no=1
for line in data:
    record=line.rstrip("\n").split("#")
    name=record[0]
    basic=int(record[1])
    da=round(basic*0.3)
    hra=round(basic*0.1)
    total=basic + da + hra
    pf=round((basic+da)*0.1)
    
    print(" {:>4d}. {:<25s} {:>6d} {:>6d} {:>6d} {:>6d} {:>6d}".
          format(s_no,name,basic,da,hra,total,pf))
 
    s_no+=1
print("-"*68)
file.close()


'''Q-13
Program to accept name, amount collected from student and house(e.g. Chenab, 
Ganges...) of any 5 students, store in file STUDENT.TXT then print the given 
output of the given house.
'''
#to store 5 records
file=open('student.txt',"w")
for i in range(5):
    print("For Student",i+1,":-")
    name=input("Enter name of the Student: ")
    amt=input("Enter amount colected: ")
    house=input("Enter student's house: ")
    record=name+"#"+amt+"#"+house+"\n"
    file.write(record)
    file.flush()
    print("*"*50)
file.close()
print("-"*100)

#to display output
file=open('student.txt',"r")
data=file.readlines()
m_house=input("Enter House whose record you want to see: ")
print()
print("-"*51)
print("{:^25s} {:^8s} {:^16s}".format("Name of Student","House","Amount Collected"))
print("-"*51)

for line in data:
    record=line.rstrip("\n").split("#")
    name, amount, house=record
    if m_house==house:
        print("{:<25s} {:<8s} {:>16s}".format(name, house, amount))
print("-"*51)
file.close()


'''Q-14
Program to access element of STACK using given menu.
'''
def push_stack(stack,item):
    '''
    To push an element into the Stack. 

    Parameters
    ----------
    stack : LIST
        list of numeric characters.
    item : NUMERIC
        Element to be pushed in stack.

    '''
    stack.append(item)
    print(item,"pushed successfully into stack.")

def pop_stack(stack):
    '''
    To pop last element of the stack.

    Parameters
    ----------
    stack : LIST
        list of numeric characters.

    '''
    if len(stack)==0:
        print("Stack Underflow !!!")
    
    else:
        top=len(stack)-1
        top_element=stack.pop(top)
        print("Element",top_element," poped.")
        

def display_stack(stack):
    '''
    To view stack.

    Parameters
    ----------
    stack : LIST
        list of numeric characters.

    '''
    length=len(stack)
    if length==0:
        print("Stack is empty.")
        
    else:
        print("Stack is: ")
        for i in range(len(stack)-1, -1, -1):
            print("\t",stack[i])

#--------------------main--------------------------
stack=[] 
menu='''
----------------------------------
| {:^30s} |
----------------------------------
| {:<30s} |
| {:<30s} |
| {:<30s} |
| {:<30s} |
----------------------------------
'''.format("MENU",
            "1. Push.",
            "2. Pop.",
            "3. View stack contents.",
            "4. QUIT."
            )

while True:
    print(menu)
    act=input("Enter the serial number of the task you want to perform: ")
    
    if act=='1':
        item=int(input("Enter new element: "))
        push_stack(stack, item)
        
    elif act=='2':
        pop_stack(stack)
        
    elif act=='3':
        display_stack(stack)
        
    elif act=='4':
        print("Thank you for using this program.")
        break
    
    else:
        print("Please enter valid number !!!")


"""Q-15
Program to store any 10 integers in random order then write a sort() function 
to sort the data in ascending order and print the content of an array.
"""
#to store integers in a array
from random import randint
l=[randint(1, 100) for i in range(10)]
    
def sort_array(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>-1 and key<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
        
print("Before: ",l)
sort_array(l)
print("After:  ",l)


'''Q-16
Write a function binary_search() to search an element Item in the given list and display a suitable 
message.
'''
def binary_search(array,item):
    beg,end=0,len(array)
    count=0
    while beg!=end:
        if item not in array:
            print(item,"not found in list.")
            break
        count+=1
        mid=int((beg+end)/2)
        if item==array[mid]:
            print(item,"found at position",mid)
            print("No. of attempts:",count)
            break
        elif item<array[mid]:
            end=mid
        elif item>array[mid]:
            beg=mid


'''Q-17
Add a book and to remove book from the queue having list of books.
'''
books=[]
front=None
rear=None
def push(queue,item):
    global front, rear
    queue.append(item)
    front,rear=0,len(queue)-1
    print(item,'enqueued successfully.')
    
def pop(queue):
    global front, rear
    if len(queue)==0:
        print("Queue Underflow !!!")
    else:
        item=queue.pop(0)
        front,rear=0,len(queue)-1
        print(item,"dequeued successfully.")
        
#---------------------------------main-----------------------------------------
menu="""
--------------
| {:^10s} |
--------------
| {:<10s} |
| {:<10s} |
| {:<10s} |
--------------""".format('MENU','1. Push','2. Pop','3. Quit')
while True:
    print(menu)
    act=input("Enter serial number of task you want to perform: ")
    if act =='1':
        book=input("Enter book name: ")
        push(books, book)
        
    elif act=='2':
        pop(books)
        
    elif act=='3':
        print("Thanks for using this program.")
        break

'''Q-18
Program to read a text file ‘english.txt’ and display the number of vowels / 
consonants /uppercase/ lowercase characters available in the file.
'''
from string import ascii_lowercase
with open('english.txt','r') as file:
    data=file.readlines()
    count_vowels=0
    count_consonants=0
    count_uppercase=0
    count_lowercase=0
    for line in data:
        for ch in line.rstrip('\n'):
            if ch not in (" ", "."):
                if ch.lower() in ['a','e','i','o','u']:
                    count_vowels+=1
                else:
                    count_consonants+=1
            
                if ch in ascii_lowercase:
                    count_lowercase+=1
                else:
                    count_uppercase+=1
        
    file.close()
    
print("No. of VOWELS: ",count_vowels)
print("No. of CONSONANTS: ",count_consonants)
print("No. of LOWERCASE characters: ",count_lowercase)
print("No. of UPPERCASE characters: ",count_uppercase)


"""Q-19
Program to create a binary file ‘result.dat’ with roll number, name and marks 
of any 5 students then input a roll number and update the marks.
"""
from pickle import dump, load
from os import rename, remove

class student:
    def __init__(self, mname='', mroll=0, mmarks=''):
        self.name=mname
        self.roll=mroll
        self.marks=mmarks
        
    def dispay_rec(self):
        print("| {:>8s} | {:<20s} | {:>5s} |".format(self.roll+'.', self.name,
                                                      self.marks))
        print("-"*43)
                                      
    def input_data(self):
        self.roll=input("Enter Student's Roll No.: ")
        self.name=input("Enter Student's Name: ")
        self.marks=input("Enter Student's Marks: ")
    
    def modify(self):
        self.marks=input("Enter new marks: ")
        

#---------------------------------main-----------------------------------------
#to store 5 records
with open('result.dat','wb') as file:
    for i in range(5):
        print("For Student",i+1,":-")
        student1=student()
        student1.input_data()
        dump(student1,file)
        print('*'*80)
        file.flush()
    file.close()
print("Records stored successfully.")

#to update marks
roll=input("Enter roll no.: ")
student1=student()
with open('result.dat',"rb") as file1:
    with open('new.dat',"wb") as file2:
        count=0
        try:
            while True:
                student1=load(file1)
                if student1.roll==roll:
                    student1.modify()
                    dump(student1, file2)
                    file2.flush()
                    count+=1
                    print("Marks updated successfully.")
                else:
                    dump(student1, file2)
                    file2.flush()
        except EOFError:
            file1.close()
            file2.close()
            if count==0:
                print("Roll no. not found!")
                
remove('result.dat')
rename('new.dat', 'result.dat')

#to display record
with open('result.dat',"rb") as file:
    student1=student()
    print()
    print("-"*43)
    print("| {:^8s} | {:^20s} | {:^5s} |".format("Roll No.", "Name", "Marks"))
    print("-"*43)

    try:
        while True:
            student1=load(file)
            student1.dispay_rec()
    except EOFError:
        file.close()


"""Q-20
Write a program to take a sample of ten phishing e-mails from file ‘email.txt’
and find most commonly occurring word.
"""
# to take 10 samples
from random import randint
sample=[]
i=0
with open('email.txt', "r") as file:
    data=file.readlines()
    file.close()
while i!=10:
    email=data[randint(0, len(data)-1)]
    if email not in sample:
        sample.append(email)
        i+=1
        
# to find most occuring word
words=[word.rstrip("\n").rstrip('.').lower() for email in sample 
        for word in email.split()]

stopwords=['to','the','and','or','you','your','with','have','had','has','of',
            'in','our','is','for','it','will']
max_count=0
for word in words:
    if word not in stopwords:
        count=words.count(word)
        if count>max_count:
            max_count=count
            max_word=word
print("The most common occuring word is:", max_word)
print("It appears", max_count, "times.")


"""Q-21
Write a program to a create Mysql table to store adno,name and fees paid by 
students in a table fees then read all the record using python function 
display() to display the data stored in a table.
"""
import pymysql as sqltor
mycon=sqltor.connect("localhost", "root", "nitin", "practical")
cursor=mycon.cursor()

# to create table fees
cursor.execute('create table fees(adno char(7) primary key, name varchar(20), fees_paid varchar(3))')
mycon.commit()
print("Table 'fees' created successfully.")

# to add records
while True:
    adno=input("Enter Addmission No. :")
    name=input("Enter Name: ")
    fees=input("Fees Paid(Yes/No): ")
    command="insert into fees values('{}', '{}', '{}')".format(adno, name, fees)
    cursor.execute(command)
    mycon.commit()
    act=input("Add more records([y]/n)? ")
    if act=="n":
        print("Records stored successfully.")
        break
    
def display():
    """
    To display records
    """
    cursor.execute("select * from fees")
    data=cursor.fetchall()
    print("-"*46)
    print("| {:^7s} | {:^20s} | {:^9s} |".format("Adno.", "Name", "Fees_Paid"))
    print("-"*46)
    for rec in data:
        print("| {} | {:<20s} | {:>9s} |".format(rec[0], rec[1], rec[2]))
        print("-"*46)
    
display()


"""Q-22
Program to create Mysql table to store mobile model and price of any five 
mobiles and then using function update_data() update the price of mobile by 
10% for all mobiles and display all updated records.
"""
import pymysql as sqltor
mycon=sqltor.connect("localhost", "root", "nitin", "practical")
cursor=mycon.cursor()

# to create table
cursor.execute("create table mobiles(model varchar(10), price int(7));")
mycon.commit()
print("Table created successfully.")

# to store 5 records
for i in range(5):
    model=input("Enter mobile model: ")
    price=int(input("Enter price: "))
    cursor.execute("insert into mobiles values('{}', {});".format(model, price))
    mycon.commit()

def update_data():
    """
    To update the price of mobile by 10% for all mobiles.
    """
    cursor.execute("update mobiles set price=price*(1+0.1);")
    mycon.commit()
    print("Records updated successfully.")
    
def display_records():
    """
    To display records.
    """
    cursor.execute("select * from mobiles;")
    data=cursor.fetchall()
    count=cursor.rowcount
    print("-"*34)
    print("| {:^5s} | {:^10s} | {:^9s} |".format("S.No.", "Model", "New_Price"))
    print("-"*34)
    s_no=0
    for rec in data:
        s_no+=1
        print("| {:>4d}. | {:<10s} | {:>9d} |".format(s_no, rec[0], rec[1]))
        print("-"*34)
    print("No. of Records:",count)
    
update_data()
display_records()


"""Q-23
Program to insert a new record in sql table employee using function Data_entry().
"""
from pymysql import connect
mycon=connect("localhost", "root", "nitin", "practical")
cursor=mycon.cursor()

def data_entry():
    """
    To insert new records in sql table employee.
    """
    empid=input("Enter Employee ID: ")
    name=input("Employee's Name: ")
    post=input("Employee's Post: ")
    mobile=input("Employee's Mobile No.: ")
    command="""insert into employee values('{}', '{}', '{}', {});""".format(
        empid, name, post, mobile)
    cursor.execute(command)
    mycon.commit()
    print("Record inserted successfully.")
    
data_entry()


"""Q-24
Write a function Delete_record() to remove the record from Mysql table lib.
"""
from pymysql import connect
mycon=connect("localhost", "root", "nitin", "practical")
cursor=mycon.cursor()

def delete_record():
    """
    To delete a record from table lib
    """
    accno=input("Enter Account No.: ")
    cursor.execute("delete from lib where accno='{}'".format(accno))
    mycon.commit()
    print("Record with Account no.",accno,"deleted successfully.")
    
delete_record()


"""Q-25
Write a program to add a new column email char(30) in Mysql table Users.
"""
from pymysql import connect
mycon=connect("localhost", "root", "nitin", "practical")
cursor=mycon.cursor()

cursor.execute("alter table users add email char(30);")
mycon.commit()
print("New column 'email' added successfully.")

                        ------x----x----x------