#guess the number.
import random
n=random.randint(1,10)
x=0
while x<5:
    A=int(input("guess the number: "))
    if A==n:
        print("you win! XD")
        break
    else:
        print("try again.")
        x+=1
else:
    print("you lose! :(")
