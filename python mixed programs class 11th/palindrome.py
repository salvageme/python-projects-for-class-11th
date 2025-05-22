#palindrome
temp=int(input("enter number: "))
num=temp
rev=0
while num:
    q=num%10
    num=num//10
    rev=rev*10+q
print("reverse of the number is:",rev)
if rev==temp:
    print(temp,"is a palindrome.")
else:
    print(temp,"is not a palindrome.")
