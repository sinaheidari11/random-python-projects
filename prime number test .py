#this code is only for numbers to understand wheter the number given is prime or not 
n=int(input("please enter a number greater than 1 : "))
prime= True
for i in range (2,n):
    if(n%i==0):
        prime=False
if prime:
    print("the number given is prime")
else:
    print("the number given is not prime")            
