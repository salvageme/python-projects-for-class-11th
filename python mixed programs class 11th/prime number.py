A=int(input("enter number: "))
x=int((A/2)+1)
for i in range(2,x):
    B=A%i
    if B==0:
        print(A,"is not a prime number.")
        break
else:
    print(A,"is a prime number.")
