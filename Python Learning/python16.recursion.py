def reverse_num(n):
    if n==0:
        return 
    print(n)
    reverse_num(n-1)
print( reverse_num(10))