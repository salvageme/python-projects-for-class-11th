#alphabet triangle pattern 2.
a=int(input("enter number of rows: "))
x=ord("A")
y="A"
for i in range(a):
    print(y)
    y=y+chr(x+1)
    x=x+1
print()
