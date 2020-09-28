#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
import math

n= input("Enter a number")
n= str(n)


if "." in n :
    print("the number is not an integer")

else:
    print("the number is an integer")
