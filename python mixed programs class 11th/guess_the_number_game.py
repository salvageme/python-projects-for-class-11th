#guess the number.
B='yes'
while B=="yes":
    import random
    n=random.randint(1,10)
    x=0
    while x<5:
        A=int(input("guess the number: "))
        if A==n:
            print("you win! XD")
            break
        else:
            x+=1
            if x<5:
                print("try again.")
            else:
                continue
    else:
        print("you lose! :(")
        print("the answer was: ",n)
    print("   ")
    print('''ok, now you choose a number between 1 and 10(included).
i will try to guess the number now.''')
    y=0
    Q=[1,2,3,4,5,6,7,8,9,10]
        ############################################################
    while y<5:
        n=random.choice(Q)
        print("is your number",n,"?(yes/no)")
        a=input()
        if a=='no':
            Q.remove(n)
            y=y+1
            continue
        else:
            print("I won!")
            break
    else:
        print("you won!")
    B=input("do you want to play again?(yes/no): ")
    if B=='yes':
        continue
    else:
        print("ok then, goodbye!")
        break
