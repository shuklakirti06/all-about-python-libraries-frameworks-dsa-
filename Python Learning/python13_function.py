def factorial(n):
    fact =1
    for i in range (1,n+1):
        fact = fact * i
    return fact
num=int(input("enter your number"))
print("factorial", factorial (num))


#
def sum(n):
    sum =0
    for i in range(1,n+1):
        sum = sum + i
    return sum 
num=int(input("enter the number"))
print("sum", sum(num))