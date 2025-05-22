#decimal to binary converter.
A=int(input("enter a decimal number: "))
B=[]
while A>=0:
    B.append(A%2)
    A=A//2
    if A==0:
        break
B.reverse()
for i in B:
    print(i,end="")
