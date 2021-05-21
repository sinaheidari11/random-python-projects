def factorial (n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
num = int(input("Enter a number greater than 1: "))

print (factorial (num))
