#largest prime number.
a=int(input("enter a number: "))
for i in range(a,1,-1):
    for j in range(2,i-1):
        if i%j==0:
            break
    else:
        print(i,"is the largest prime number.")
        break

