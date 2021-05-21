""" Calculator
----------------------------------------
"""

def addition ():
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0 
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]
def subtraction ():
    print("Subtraction");
    n = float(input("Enter the number: "))
    t = 0 
    sum = 0
    while n != 0:
        ans = ans - n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]
def multiplication ():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0
    ans = 1
    while n != 0:
        ans = ans * n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]
def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]

while True:
    list = []
    print(" Simple Calculator in python.")
    print(" Enter '+' for addition")
    print(" Enter '-' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'a' for average")
    print(" Enter 'q' for quit")
    c = input(" ")
    if c != 'q':
        if c == '+':
            list = addition()
            print("Answer = ", list[0], " total inputs ",list[1])
        elif c == '-':
            list = subtraction()
            print("Answer = ", list[0], " total inputs ",list[1])
        elif c == 'm':
            list = multiplication()
            print("Answer = ", list[0], " total inputs ",list[1])
        elif c == 'a':
            list = average()
            print("Answer = ", list[0], " total inputs ",list[1])
        else:
            print ("Sorry, invilid character")
    else:
        break
