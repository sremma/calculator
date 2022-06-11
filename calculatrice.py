

(""" PYTHON CALCULATOR 

OPERATIONS:
1- ADD
2- SUBTRACT
3- MULTIPLY              
4- DIVIDE
5- EXPONENTIATION
6- SQUARE ROOT
7- FACTORIAL

press '0' to end operations...

""")
import time
import math

while True:
    
    operation = int(input(" Select operations from '1,2,3,4,5,6,7' : "))
    
    if(operation == 0):
        print("Operation is ending...")
        time.sleep(2)
        print("See you again... ")
        break
        
    elif(operation == 1):
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        print("Please wait...")
        time.sleep(1)
        print("{} + {} = {}".format(n1,n2,n1 + n2))
        
    elif(operation == 2):
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        print("Please wait...")
        time.sleep(1)
        print("{} - {} = {}".format(n1,n2,n1 - n2))
        
    elif(operation == 3):
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        print("Please wait...")
        time.sleep(1)
        print("{} x {} = {}".format(n1,n2,n1 * n2))
        
    elif(operation == 4):
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        print("Please wait...")
        time.sleep(1)
        print("{} / {} = {}".format(n1,n2,n1 / n2))


    elif(operation == 5):
        n1 = int(input("Enter number: "))
        print("Please wait...")
        time.sleep(1)
        x = math.sqrt(n1)
        print("{} Squared equals {}".format(n1,math.sqrt(n1)))
        
    elif(operation == 6):
        n1 = int(input("Enter base number: "))
        n2 = int(input("Enter exponent number: "))
        print("Please wait...")
        time.sleep(1)
        x = math.pow(n1,n2)
        print("{} to the power {} = {} ".format(n1,n2,math.pow(n1,n2)))
        
        
    elif(operation == 7):
        while True:
            n1 = int(input("Enter number: "))
            factorial = 1
            for i in range(2,n1+1):
                factorial *= i
            print("Factorial:",factorial)
            break
        
    else:
        print("Invalid input")
        