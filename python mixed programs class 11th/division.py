#quotient calculater.
for i in range(1,11):
    print("enter 2 numbers.")
    A=int(input("enter numerater: "))
    B=int(input("enter denominater: "))
    if B==0:
        print("denominater cannot be zero. aborting!")
        continue
    else:
        C=A//B
        print("quorient=",C)
