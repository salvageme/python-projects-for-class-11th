# sum and non duplicate sum calculater.
A=int(input("enter first number: "))
B=int(input("enter second number: "))
C=int(input("enter third number: "))
X=A+B+C
Y=0
if A!=B and A!=C:
    Y+=A
elif B!=A and B!=C:
    Y+=B
elif C!=A and C!=B:
    Y+=C
print("sum of the numbers is:",X)
print("non duplicate sum is:",Y)
