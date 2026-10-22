s1={1,45,6,78}
s2={7,8,1,78}
print(s1.union(s2))
print(s1.intersection(s2))


# dictionary examples:

marks ={
    "hindi" : 45,
    "maths": 78,
    "english": 67,
    "science":54
}
highest = 0
highest_subject=" "
for subject,score in marks .items():
    if score > highest:
        highest = score
        highest_subject = subject
print("highest subject", highest_subject)
print("marks", highest)




