# for square root of number "a", where a>0;
# 1- analyze the known square roots before and after sqrt of "a"
# 2- choose an initial guess "x0" for sqrt of "a", x0>0
# 3- use Xn+1 = 1/2*(Xn + a/Xn) to find the next guess 
# 4- repeat untill decimal places of Xn+1 and Xn are the same or desired accuracy is reached

import math

def HeronsMethod(a, x0):
    if a <= 0:
        return "a must be greater than 0 for Heron's Method to work"
    else:
        Xn = x0
        Xn1 = 1/2*(Xn + a/Xn)
        return Xn1

# a = 2
# x0 = 1
# d = 5

an = input("Enter a number to find the square root: ")
# print(an)
a=int(an)

x = input("Enter an initial guess for the square root: ")
# print(x)
x0=int(x)

dP = input("Enter the number of decimal places to compute: ")
# print(d)
d=int(dP)

print()


print("Square Root of", a, "is:", round(math.sqrt(a),d), "up to",d, "decimal places") 
print()


print("Herons Method computations")
print("X 0 =", x)
for i in range(d):
    x0 = round(HeronsMethod(a, x0),d)
    print("X",i+1,"=",x0)
    

