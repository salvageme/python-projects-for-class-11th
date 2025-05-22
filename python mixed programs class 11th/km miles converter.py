# km-mile converter.
print ("which unit do you want to change? ")
A =input()
X =['Km','km']
Y =['mile','miles']
B =float(input("enter value"))
if A==X:
    print ("value in miles is:  ",B*0.6)
elif A==Y:
    print ("value in km is:  ",B*1.6)
    
