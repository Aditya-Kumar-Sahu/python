"""
Program to create a data file and store data in it as an object
"""
import pickle
class hotel:
    def __init__(self,mtableno=0,mitem="",mrate=0,mno_of_plates=0,mrecord=tuple()):
#       Constructor function
        self.tableno=mtableno
        self.item=mitem
        self.price=mrate
        self.no_of_plates=mno_of_plates
        self.record=mrecord
        
    def Order_Entry(self):
#       function to take data from user
        self.tableno=input("Enter the table number: ")
        ans="y"
        while ans=="y":
            self.item=input("Enter name of the item: ")
            self.no_of_plates=input("Enter no of plates for above item: ")
            self.price=input("Enter the rate of the item: ")
            amount=int(self.no_of_plates)*int(self.price)
            self.record+=(self.item+"#"+self.no_of_plates+"#"+self.price+"#"+str(amount),)
            ans=input("Is there more items you want to enter(y/n): ")
            
    
    def Print_Bill(self):
#       function to dislay data stored
        print("{:^50s}".format("HOTEL PRINCE")) 
        print("{:^50s}".format("C C BHILAI"))
        print("Table No.",self.tableno)
        print("-"*50)
        print("| {:^15s} | {:^12s} | {:^4s} | {:^6s} |".format("ITEM NAME","NO OF PLATES","RATE","AMOUNT"))
        print("-"*50)
        total=0
        for data in self.record:
            a,b,c,d=data.split("#")
            print("| {:<15s} | {:>12s} | {:>4s} | {:>6s} |".format(a,b,c,d))
            print("-"*50)
            total+=int(d)
        print("{:>40s}".format("TOTAL AMOUNT:"),total,"\n\n")
        
#------------------------------main------------------------------
        
task="""\n           MENU
    1. Add new entry.
    2. View stored entry.
    3. Quit."""
print(task)

act=input("Enter serial number of the task you want to perform: ")
while True:
    if act=="1":
        file=open("hotel.dat","ab")
        record1=hotel()
        record1.Order_Entry()
        pickle.dump(record1,file)
        file.flush()
        file.close()
        
    elif act=="2":
        record1=hotel()
        file=open("hotel.dat","rb")
        try:
            while True:
                record1=pickle.load(file)
                record1.Print_Bill()
        except EOFError:
            file.close()
    else:
        print("Thank You for using this Program")
        break
    print(task)
    act=input("Enter serial number of the task you want to perform: ")    

    