# character identifier.
ch=input("enter a single character: ")
if ch>='A' and ch<='Z':
    print("you entered an upper case character.")
elif ch>='a' and ch<='z':
    print("you entered a lower case character.")
elif ch>='0' and ch<='9':
    print("you entered a number.")
elif ch==' ':
    print("you entered a space.")
else:
    print("you entered a special character.")
