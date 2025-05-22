# area and perimeter calculater.
print("what would you like to calculate?(area/perimeter)- ")
A=input()
B=float(input("enter length: "))
C=float(input("enter width: "))
if A=='area':
    print("the area is:",B*C)
else:
    print("the perimeter is:",2*(B+C))
