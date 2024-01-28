#!/usr/bin/env python
# coding: utf-8

# 1. Modify your greeting program so that if the user does not enter a name (i.e. they
# just press enter), the program responds "Hello, Stranger!". Otherwise it should print
# a greeting with their name as before
# 

# In[8]:


name=input("Please enter your name")
if name.lower() or name.upper():
    print("Hello",name)
else:
    print("Hello Stranger")


# Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again. If the two
# passwords entered are the same the program should say "Password Set" or
# similar, otherwise it should report an error.

# In[10]:


new_pswd=input("Enter a new password")
confirm_pswd=input("Enter to confirm")
if new_pswd==confirm_pswd:
    print("Password Set")
else:
    print("An error is reported")


# Modify your previous program so that the password must be between 8 and 12
# characters (inclusive) long.

# In[13]:


print("Choose your password")
print("Your password must contain 8 to 12 characters")
new_pswd=input("Enter a new password")
confirm_pswd=input("Enter to confirm")
if new_pswd==confirm_pswd:
    if len(new_pswd)==8 or len(new_pswd)==12:
        print("Password Set")
    else:
        print("Please apply the conditions")
else:
    print("An error is reported")


# Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# In[37]:


print("Choose your password")
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
new_pswd=input("Enter a new password")
confirm_pswd=input("Enter to confirm")
if new_pswd==confirm_pswd:
    if len(new_pswd)==8 or len(new_pswd)==12:
        if new_pswd in BAD_PASSWORDS:
            print("The password is not allowed")
        else:
                print("password set")
    else:
        print("please apply the condition")
else:
    print("An error is reported")


# Modify your program a final time so that it executes until the user successfully
# chooses a password. That is, if the password chosen fails any of the checks, the
# program should return to asking for the p
# assword the first time.

# In[38]:


BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    print("Choose your password")
    print("Your password must contain 8 to 12 characters")
    
    while True:
        new_pswd=input("Enter a new password")
        confirm_pswd=input("Enter to confirm")
        if new_pswd==confirm_pswd:
            if len(new_pswd)==8 or len(new_pswd)==12:
                if new_pswd in BAD_PASSWORDS:
                    print("The password is not allowed")
                else:
                    print("password set")
                    break
            else:
                print("please apply the condition")
        else:
            print("An error is reported")
    break


# Write a program that displays the "Seven Times Table". That is, the result of
# multiplying 7 by every number from 0 to 12 inclusive. The output might start:
# 0 x 7 = 0
# 1 x 7 = 7
# 2 x 7 = 14
# and so on

# In[43]:


print("Seven Times Table")
print("multiplication table of 7")
for i in range(1,13):
     print(7,"*",i,"=",7*i)


# Modify your "Times Table" program so that the user enters the number of the table
# they require. This number should be between 0 and 12 inclusive

# In[44]:


print("Times Table")
num=int(input("enter the number you want"))
print("multiplication table of",num)
for i in range(1,13):
     print(num,"*",i,"=",num*i)


# Modify the "Times Table" again so that the user still enters the number of the table,
# but if this number is negative the table is printed backwards. So entering "-7"
# would produce the Seven Times Table starting at "12 times" down to "0 times"

# In[46]:


print("Times Table")
num=int(input("enter the number you want"))
print("multiplication table of",num)
if num<0:
    print("printing number from 12")
    for i in range(12,0,-1):
        print(num,"*",i,"=",num*i)
else:
    for i in range(1,13):
        print(num,"*",i,"=",num*i)
    

