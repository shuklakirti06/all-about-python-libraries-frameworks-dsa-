
#sum of even numbers

def even_numbers(n):
    sum=0
    for i in range(1,n+1):
     if i% 2==0:
        sum = sum +i
     
    return sum
num=int(input("enter your even number :"))
print("your sum of even numbers are :",even_numbers(num))

# now sum of odd numbers

def odd_numbers(n):
    sum =0
    for i in range(1,n+1):
        if i % 2!= 0:
            sum = sum + i
    return sum

num=int(input("enter the odd numbers:"))
print("your sum of odd numbers is :", odd_numbers(num))


# count of even numbers from 1 to n

def even_numbers(n):
    count = 0
    for i in range (1, n+1):
        if  i%2== 0:
            count= count +1
    return count
numb=int(input(" enter your number"))
print("your count of even numbers is :", even_numbers(numb))


