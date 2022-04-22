'''
Program to store records in a file
'''

import csv
def mobile_recharge():
#   Function to store new record
    dic={'BSNL':[50,100,200,500,1000], 'JIO':[49,101,159,299],'Airtel':[59,129,499,1999]}
    mob=input("Enter your mobile number: ")
    date=input("Enter todays date(dd/mm/yy): ")
    isp=input("Enter name of service provider: ")
    amt=int(input("Enter amount: "))
    
    while True:
        if amt in dic[isp]:
            break
        else:
            amt=int(input("Please enter valid amount: "))
    
    csv.writer(open('recharge.csv','a'), delimiter=",").writerow([mob, date, amt, isp])
        
def daily_collection():
#   Function to display stored record
    data=csv.reader(open('recharge.csv',"r"))
    total=0
    
    print("\t{:^72s}\n\t{:^72s}\n".format("BHUMIKA CELLPHONE LTD.", "BHILAI"))
    print("\t","-"*72)
    print("\t","| {:^13s} | {:^15s} | {:^16s} | {:^15s} |".format("Recharge Date","Customer Mobile","Service provider","Recharge Amount"))
    print("\t","-"*72)
    
    for rec in data:
        if rec!=[]:
            print("\t","| {:>13s} | {:>15s} | {:>16s} | {:>15s} |".format(rec[1],rec[0],rec[3],rec[2]))
            print("\t","-"*72)
            total+=int(rec[2])
    print("\t","{:>70s}".format("TOTAL AMOUNT: RS "+str(total)))
    print("\n\n\t","Cashier Sign")
    
#----------------------------main----------------------------
print("""\t1. Do a top up.
\t2. View stored data.""")
act=input("Enter the serial number of the task you want to perform: ")

if act=="1":
    ans="y"
    while ans=="y":
        print()
        print("""   Available top ups are:\n
BSNL Recharge: Rs 50, 100, 200, 500, 1000
JIO Recharge: Rs 49, 101, 159, 299 
Airtel Recharge: Rs 59, 129, 499, 1999""")
        mobile_recharge()
        ans=input("\nDo you want to enter more records(y/n): ")
    print("\nThanks for using the Program.")
    
elif act=="2":
    print()
    daily_collection()
    print("\nThanks for using the Program.")
    