#!/usr/bin/env python
# coding: utf-8

# Last week you wrote a program that printed out a cheery greeting including your
# name. Take a copy of it, and modify it so that the user enters their name at the
# keyboard, and then receives a greeting. For example:
# Hello, what is your name? Mr Apricot
# Hello, Mr Apricot. Good to meet you!
# 

# In[2]:


name = input("Hello, what is your name? ")
print(f"Hello, {name}. Good to meet you!")


# Write a program that prompts a user to enter a temperature in Celsius, and then
# displays the corresponding temperature in Fahrenheit, like so:
# Enter a temperature in Celsius: 32.5
# 32.5C is equivalent to 90.5F.

# In[4]:


temp_celsius = float(input("Enter a temperature in Celsius: "))
temp_fahrenheit = temp_celsius * 9/5 + 32
print(temp_celsius,"C is equivalent to",temp_fahrenheit,"F.")


# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is usually 24 students, but this is
# sometimes varied to create groups of similar size. Write a program that prompts for
# the number of students and group size, and then displays how many groups will be
# needed and how many will be left over in a smaller group.
# How many students? 113
# Required group size? 22
# There will be 5 groups with 3 students left over.
# For bonus credit, see if you can fix the grammar in the output. So if there were 101
# students in groups of 20 the output would be:
# There will be 5 groups with 1 student left over.
# 

# In[8]:


num_students = int(input("How many students are there? "))
group_size = int(input("What is the required group size? "))

num_groups = num_students // group_size
remainder = num_students % group_size

if remainder == 0:
    print("There will be",num_groups,"groups with no students left over.")
else:
    print(f"There will be",num_groups," groups with", remainder,"students left over.")


# A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
# first count the sweets and then divide them according to how many pupils attend
# that day. Write a program that will tell the teacher how many sweets to give to each
# pupil, and how many she will have left over.

# In[9]:


num_sweets = int(input("How many sweets are in the tub? "))
num_pupils = int(input("How many pupils are there today? "))
sweets_per_pupil = num_sweets // num_pupils
remainder = num_sweets % num_pupils
print(f"Give each pupil {sweets_per_pupil} sweets.")
if remainder == 0:
    print("There will be no sweets left over.")
else:
    print(f"There will be {remainder} sweets left over.")


# In[ ]:




