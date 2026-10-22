computer = -1
youstr=input("enter your turn(s for snake ,w for water,g for gun):").strip().lower()
youdict ={"s": 1 , "w": -1 , "g": 0}
you = youdict[youstr]

if(computer==-1 and you==1):
    print("you win")
elif (computer== -1 and you == 0):
    print("you lose!")
if(computer == 1 and you== -1):
    print("you loose")
elif(computer == 1 and you == 0):
    print("you win!")
if(computer==0 and you==1):
    print("you loose")
elif(computer == 0 and you== -1):
    print(" you win , congrats")
else:
    print("you loss , better luck next time")

