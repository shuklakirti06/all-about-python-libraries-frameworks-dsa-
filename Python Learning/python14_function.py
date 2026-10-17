def even_numbers(n):
    largest=0
    for i in range(1,n+1):
        if i %2==0 and i>largest:
            largest = largest +i
    return largest
x=int(input("enter your number"))
print("the largest number of evn number is", even_numbers(x))