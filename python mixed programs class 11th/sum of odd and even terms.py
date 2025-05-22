# sum of odd and even numbers.
A=int(input("enter number: "))
B=1
even=odd=0
while B<=A:
    if B%2==0:
        even+=B
    else:
        odd+=B
    B+=1
print("sum of all enen numbers:",even)
print("sum of all odd numbers:",odd)
