# leap year
A=int(input("enter year: "))
if A%100==0 and A%400==0:
    print(A,"is a leap year.")
elif A%100!=0 and A%4==0:
    print(A,"is a leap year.")
else:
    print(A,"is not a leap year.")
