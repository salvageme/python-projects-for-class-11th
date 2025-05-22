# arranging 3 numbers in assending order.
A=int(input("enter first number: "))
B=int(input("enter second number: "))
C=int(input("enter third number: "))
if A<B and A<C:
    if B<C:
        X,Y,Z=A,B,C
    else:
        X,Y,Z=A,C,B
elif B<A and B<C:
    if A<C:
        X,Y,Z=B,A,C
    else:
        X,Y,Z=B,C,A
elif C<A and C<B:
    if A<B:
        X,Y,Z=C,A,B
    else:
        X,Y,Z=C,B,A
print("numbers in assending order are:",X,Y,Z)
