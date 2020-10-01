#! python3

#  Have the user enter a username 
# If the username is not "admin" then tell them it is an "invalid user", 
# but if it is, then ask them for a password 
# If they get the password correct (password is 12345password) 
# then display the message "Access granted"
# 1 marks

n= input("Enter a username")
n= str(n)




if "admin" in n:
    p= input("Enter password")
    

if "12345password" in "Enter password":
    print(p)
    print("Access granted")

else:
    print("invalid user")




