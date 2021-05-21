#sum of the numbers from 1 to Number 
def sumn(Number):
    return (Number*(Number+1))/2
print (sumn(100))


def summ(number,num):
    if number ==101:
        return num
    else :
        return summ(number+1,num+number)

print("the sum of the first 100 numbers is =",summ(1,0))




    
