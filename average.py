n= int(input("how much number you are going to put in = "))

b = []

for i in range(0,n):
    element= float(input("enter your number : "))
    b.append(element)

avg = sum(b)/n
print(avg)
