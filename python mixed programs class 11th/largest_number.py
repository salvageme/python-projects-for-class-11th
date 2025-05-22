# largest number identifier.
A=float(input("enter first number: "))
B=float(input("enter second number: "))
C=float(input("enter third number: "))
X=A
if X<B:
    X=B
if X<C:
    X=C
print(X,"is the largest number")
