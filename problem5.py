#! python3

#  In math, if a quadratic equation is in the format
# ax^2 + bx + c = 0, the discriminant can be calculated as
# b^2 - 4 * a * c
# If the discriminant is a perfect square, the equation can
# be factored.  Furthermore, if the discriminant is negative,
# then the equation has no solutions (not used in this assignment).
# Have the user enter in values for a, b and c and then 
# tell them if the equation can be factored.

# Inputs:
# - 3 numbers (a, b, c)

# Outputs:
# - "the equation can be factored"
# - "the equation can not be factored"


import math


a= input("Enter a")
b= input("Enter b")
c= input("Enter c")
a= float(a)
b= float(b)
c= float(c)

discriminant= (pow(b,2))-(4*a*c)



if discriminant >= 0:
    discriminant1= float(discriminant)
    print(discriminant1)
    discriminantfloatedsqr= math.sqrt(discriminant1)
    print(discriminantfloatedsqr)
    discriminant2= int(discriminant)
    discriminantintsqr= math.sqrt(discriminant2)
    discriminantintsqr= int(discriminantintsqr)
    if discriminantfloatedsqr==discriminantintsqr:
        print("the equation can be factored")
    else:
        print("the equation can not be factored")

else:
    print("the equation can not be factored")

#q= input(
#a= float(q) 
#b= math.sqrt(a)     
#d= int(q)
#c= math.sqrt(d)
#c= int(c)