#aadvanced sum.
B=0
X=0
ans='y'
while ans=='y':
    A=int(input("enter number: "))
    B=B+A
    if A<0:
        print("entered number cannot be less than zero.")
        continue
    X=X+1
    ans=input("would you like to enter another number?(y/n): ")
else:
    print("you have entered",X,"numbers till now.")
print("sum=",B)
