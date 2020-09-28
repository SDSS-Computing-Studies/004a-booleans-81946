#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"

n= input("Enter a number")
n= float(n)

if n>0:
    print("The number is positive")
elif n<0:
    print("The number is negative")
else:
    print("The number is 0")