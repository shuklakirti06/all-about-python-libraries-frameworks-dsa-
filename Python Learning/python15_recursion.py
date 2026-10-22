# RECURSION:-
            # recursion means ek function ka khud ko hi call krna jab tak condition puri na ho jaye
def print_num(n):
    if n > 5:
       return
    print(n)
    print_num(n+1)
print_num(1)

# factorial example
def fact(n):
    if n ==1:
        return 1
    return n *fact(n-1)
print(fact(6))


# sum of first n numbers 

def total (n):
  if n==1:
    return 1
  return n+total(n-1)
print(total(5))