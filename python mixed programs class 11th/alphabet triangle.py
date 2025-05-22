#alphabet triangle pattern.
a=int(input("enter number of rows: "))
x=ord("A")
y="A"
for i in range(a):
    for j in range(i+1):
        print(chr(x),end=' ')
        x=x+1
    print()
