#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
import math

n= input("Enter a side length")
o= input("Enter another side length")
q= input("Enter another side length")
n= float(n)
o= float(o)
q= float(q)

if n < o and n < q:
    n= n

if o <n and o < q:
    o= n

if q < o and q < n:
    q= n
# decide which is the hypotenuse
# c= whichever one is the hypotenuse
# a = smallest
# b = middle number

# then you can go ahead and see if a**2 + b**2 == c**2
print(n, q, o, sep=" ")

a= (pow(n,2))
b= (pow(q,2))

c= (pow(o,2))

ee= a+b # expected hypotenuse

bot= math.sqrt((c/1.02)*c)
# lower limit
bo= bot - c
#bo = lower limit - actual hypotenuse
p= c-bo


if ee > bot and ee < p:
    print("that is a right triangle")

elif ee < p:
    print("that is an obtuse triangle")

elif ee > bot:
    print("that is an acute triangle")



