"""
Program to perform basic binary operations: add, subtract, multiply, divide
"""

def add(a,b):
    """
    to add a and b
    """
    return a+b

def subtract(a,b):
    """
    to subtract b from a
    """
    return a-b

def multiply(a,b):
    """
    to multiply a and b
    """
    return a*b

def divide(a,b):
    """
    to divide a by b, b!=0
    """
    if b!=0:
        return a/b
    else:
        return "Undefined, division by zero"

#----------------------------------main--------------------------------------
menu="""
1. Add
2. Subtract
3. Multiply
4. Divide
"""
run=True
while run:
    print()
    print(menu)
    operation=int(input("Enter operation(1/2/3/4): "))
    if operation in (1,2,3,4):
        num1=float(input("Enter First number: "))
        num2=float(input("Enter Second number: "))
        print()
        if operation==1:
            print(num1, "+", num2, "=", add(num1, num2))
        elif operation==2:
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif operation==3:
            print(num1, "x", num2, "=", multiply(num1, num2))
        elif operation==4:
            print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input!")
        continue

    print()
    act=input("Want to do more calculations([y]/n)? ")
    if act=="n":
        print("Thanks for using this program.")
        run=False

#                           ---x--x--x---