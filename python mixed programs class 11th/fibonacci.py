# fibonacci series.
A=int(input("enter : "))
n=0
m=1
i=0
print(n)
print(m)
while i<=A:
    s=n+m
    print(s)
    n=m
    m=s
    i=i+1
