#string palindrome.
A=input("enter word: ")
L=len(A)
B=""
for i in range(L-1,-1,-1):
    B=B+A[i]
print("reverse of word",A,"is:",B)
if A==B:
    print(A,"is a palindrome.")
else:
    print(A,"is not a palindrome.")
