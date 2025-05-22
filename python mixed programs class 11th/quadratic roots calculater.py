# quadratic roots calculater.
import math
print('ax^2+bx+c')
A=int(input("enter value of a: "))
B=int(input("enter value of b: "))
C=int(input("enter value of c: "))
D=B**2-4*A*C
if A==0:
    print("value of a cannot be 0.")
else:
    if D>=0:
        R1=(-B-math.sqrt(D))/(2*A)
        R2=(-B+math.sqrt(D))/(2*A)
        print("roots are real and unique.")
        print('root1=',R1)
        print('root2=',R2)
    elif D==0:
        R1=-B/(2*A)
        R2=-B/(2*A)
        print("roots are real and equal.")
        print('root1=',R1)
        print('root2=',R2)
    else:
        print('roots are imaginary.')
