#decimal to binary converter.
A=int(input("enter decimal number: "))
B=A
C=0
while B:
    D=B%2
    B=B//2
    C=(C*10)+D
X=0
while C:
    Y=C%10
    C=C//10
    X=(X+Y)*10
print(A,"is binary is:",X)
