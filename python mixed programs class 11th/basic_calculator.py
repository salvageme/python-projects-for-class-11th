# basic calculater.
A=float(input("enter first number: "))
B=float(input("enter second number: "))
C=input("enter operator(+,-,*,/,//,%): ")
if C=='+':
    print(A+B)
elif C=='-':
    print(A-B)
elif C=='*':
    print(A*B)
elif C=='/':
    print(A/B)
elif C=='//':
    print(A//B)
elif C=='%':
    print(A%B)
else:
    print("invalid operator.")
