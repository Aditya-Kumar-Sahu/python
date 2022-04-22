"""
Program to create a data file and store information of employees
"""

def create_file():
#   To create a data file
    file= open("emp.dat",'w')
    head="Name of Employee#Gender#Post#Mob Number#Date of Birth#Basic Salary\n"
    file.write(head)
    file.close()
    
def append_file():
#   To store data in data file
    file=open("emp.dat","a")
    ans="y"
    while ans=="y":
        name=input("Enter name of Employee: ")
        gen=input("Enter gender of Employee(M/F): ")
        post=input("Enter post of Employee: ")
        num=input("Enter mobile number of Employee: ")
        dob=input("Enter date of birth of Employee(dd/mm/yy): ")
        salary=input("Enter the basic salary of Employee: ")
        data=name+"#"+gen+"#"+post+"#"+num+"#"+dob+"#"+salary+"\n"
        file.write(data)
        ans=input("Do you want to enter more employee's details(y/n): ")
    file.close()
    
def view_file():
#   To view data stored in data file
    file=open("emp.dat","r")
    content=file.readlines()
    for line in content:
        a,b,c,d,e,f=line.rstrip("\n").split("#")
        print("-"*98)
        print("| {:<20s} | {:^6s} | {:<15s} | {:>13s} | {:>13s} | {:>12s} |".format(a,b,c,d,e,f))
    print("-"*98)
    file.close()
    
def phone_dir():
#   To view Mobile numbers of employees
    file=open("emp.dat","r")
    content=file.readlines()
    for line in content:
        print("-"*40)
        print("| {:<20s} | {:^13s} |".format(line.rstrip("\n").split("#")[0],line.rstrip("\n").split("#")[3]))
    print("-"*40)
    file.close()
    
def emp_details():
#   to print emloyee datails Gender wise
    file=open("emp.dat","r")
    content=file.readlines()
    print("-"*98)
    head=content.pop(0)
    a,b,c,d,e,f=head.rstrip("\n").split("#")
    print("| {:<20s} | {:^6s} | {:<15s} | {:>13s} | {:>13s} | {:>12s} |".format(a,b,c,d,e,f))
    l1,l2=[],[]
    for line in content:
        a=line.split("#")
        if a[1]=="F":
            l1.append(line)
        else:
            l2.append(line)
    l=l1+l2
    for line in l:
        a,b,c,d,e,f=line.rstrip("\n").split("#")
        print("-"*98)
        print("| {:<20s} | {:^6s} | {:<15s} | {:>13s} | {:>13s} | {:>12s} |".format(a,b,c,d,e,f))
    print("-"*98)
    file.close()
    
def bday_list():
#    to print today's Birthday list of employees
    from datetime import datetime
    today=str(datetime.date(datetime.now()))
    file=open("emp.dat","r")
    content=file.readlines()
    content.pop(0)
    print("-"*24)
    print("| {:^20s} |".format("Today's B'day list"))
    for line in content:
        data=line.split("#")[4]
        if data.split("/")[0]==today.split("-")[2]:
            if data.split("/")[1]==today.split("-")[1]:
                print("-"*24)
                print("| {:<20} |".format(line.split("#")[0]))
    print("-"*24)
    file.close()
    
def salary_register():
#   to view basic salary, DA, MA, total salary of employees
    file=open("emp.dat","r")
    content=file.readlines()
    content.pop(0)
    print("-"*68)
    print("| {:^20s} | {:^12s} | {:^6s} | {:^6s} | {:^8s} |".format("Name of Employee","Basic Salary","DA","MA","Total"))
    for line in content:
        a=line.split("#")[0]
        b=line.rstrip("\n").split("#")[5]
        da=int(0.1*int(b))
        ma=int(0.15*int(b))
        ts=int(b)+da+ma
        print("-"*68)
        print("| {:<20s} | {:>12s} | {:>6d} | {:>6d} | {:>8d} |".format(a,b,da,ma,ts))
    print("-"*68)
    file.close()
    
#--------------------main----------------------
    
print("{:^34s}".format("MENU"))
task=''' 
 1. Create/Reset data file
 2. Enter new record to data file
 3. View data stored in data file 
 4. View phone Dir of Employees 
 5. View Employees' details Gender wise
 6. View today's Birthday List
 7. View salary register of employees
 8. Quit'''
print(task)

act=int(input("Enter serial number of task you want to perform:"))
while act<=8:
    if act==1:
        create_file()
    elif act==2:
        append_file()
    elif act==3:
        view_file()
    elif act==4:
        phone_dir()
    elif act==5:
        emp_details()
    elif act==6:
        bday_list()
    elif act==7:
        salary_register()
    elif act==8:
        print("Thank You for using this Program")
        break
    print(task)
    act=int(input("Enter serial number of task you want to perform:"))
    