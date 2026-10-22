marks=[]
f1=int(input("enter marks name:"))
marks.append(f1)
f2=int(input("enter marks name:"))
marks.append(f2)
f3=int(input("enter marks name:"))
marks.append(f3)
f4=int(input("enter marks name:"))
marks.append(f4)
marks.sort()
print (marks)

# tuples examples (note: tuples are immutable)
a=(3,4,5,3,3,6,3,7,8)
n=a.count(3)
print(n)

l=(34,56,78,90)
print(sum(l))

info=("kirti",21,"english")
name,age,subject=info;
print(info)