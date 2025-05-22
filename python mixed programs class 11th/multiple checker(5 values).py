# multiple checker.
A=eval(input("enter a list of five numbers: "))
X=float(input("enter diviser number: "))
print("multiples of",X,"are:-")
Y=0
if A[0]%X==0:
    print(A[0])
    Y+=1
if A[1]%X==0:
    print(A[1])
    Y+=1
if A[2]%X==0:
    print(A[2])
    Y+=1
if A[3]%X==0:
    print(A[3])
    Y+=1
if A[4]%X==0:
    print(A[4])
    Y+=1
print(Y,"multiples of",X,"found.")
