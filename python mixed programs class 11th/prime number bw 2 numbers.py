#find prime numbers between any two numbers.
a=int(input("enter first number: "))
b=int(input("enter second number: "))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            print(i,"is not a prime number!")
            break
    else:
        print(i,"is a prime number!")
