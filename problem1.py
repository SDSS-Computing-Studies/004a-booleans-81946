#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# Hint: Use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"
import math

n= input("Enter a number")
n= float(n)


if n%2==0:
    print("The number is even")
elif n%2==1:
    print("The number is odd")
