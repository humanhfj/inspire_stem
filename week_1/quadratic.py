


import math

a=float(input("Enter the coeficient of the first term : "))
b=float(input("Enter the coeficient of the second term : "))
c=float(input("Enter the  constant  : "))

d =((float(b)**2) -4 *float (a) * float(c))
x_1 =(-b + math.sqrt(d)) / 2* a
x_2 =(-b - math.sqrt(d))/ 2 * a

print("The solution of the quadratic equation")