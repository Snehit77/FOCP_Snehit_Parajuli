#!/usr/bin/env python
# coding: utf-8

# Functions are often used to validate input. Write a function that accepts a single
# integer as a parameter and returns True if the integer is in the range 0 to 100
# (inclusive), or False otherwise. Write a short program to test the function.

# In[6]:


def inclusive():
    num=int(input("enter a number"))
    if 0<=num<=100:
        print("true")
    else:
        print("false")
inclusive()
        


# Write a function that has a single string as its parameter, and returns the number of
# uppercase letters, and the number of lowercase letters in the string. Test the
# function with a short program.

# In[12]:


def check(name):
    lcase=len(name)-len(name.upper())
    ucase=len(name)-len(name.lower())
    print("no. of uppercase letters are",ucase)
    print("no. of lowercase letters are",lcase)
check("Snehit")


# Modify your "greetings" program so that the first letter of the name entered is
# always in uppercase with the rest in lowercase. This should happen even if the user
# entered their name differently. So if the user entered arthur, ARTHUR, or even
# arTHur the name should be displayed as Arthur.
# 

# In[19]:


def greetings():
    fname=input("enter your first name")
    tear=fname[0].upper()
    tear2=fname[1:].lower()
    name=tear+tear2
    print("HELLO",name)
greetings()
    


# When processing data it is often useful to remove the last character from some
# input (it is often a newline). Write and test a function that takes a string parameter
# and returns it with the last character removed. (If the string contains one or fewer
# characters, return it unchanged.)

# In[24]:


def remove_last_char(string):
    if len(string) > 1:
        return string[:-1]
    else:
        return string
print(remove_last_char("Snehit"))


# Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions. (Google will find you the formulae)

# In[26]:


def celcius():
    tempc=float(input("enter the temp in celcius"))
    tempf=(9/5*tempc)+32
    print("The temperature in Fahrenheit is",tempf)
celcius()
def fahrenheit():
    tempf=float(input("enter the temp in farhenheit"))
    tempc=5/9*(tempf-32)
    print("The temperature in Celcius is",tempc)
fahrenheit()


# Write a program that takes a centigrade temperature and displays the equivalent in
# fahrenheit. The input should be a number followed by a letter C. The output should
# be in the same format.

# In[30]:


def temp():
    tempc=input("Enter the temp in celcius in C")
    cel=float(tempc[:-1])
    tempf=(9/5*cel)+32
    print("The temperature in Fahrenheit is",tempf,"F")
temp()


# Write a program that reads 6 temperatures (in the same format as before), and
# displays the maximum, minimum, and mean of the values.
# Hint: You should know there are built-in functions for max and min. If you hunt, you
# might also find one for the mean

# In[37]:


temperatures = []
def mean(lst):
    return sum(lst) / len(lst)
for i in range(6):
    temp = input("Enter temperature " + str(i+1) + "in C : ")
    cel=float(temp[:-1])
    temperatures.append(temp)
    
max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = mean(temperatures)

print("Maximum Temperature: ", max_temp)
print("Minimum Temperature: ", min_temp)
print("Mean Temperature: ", mean_temp)


# Modify the previous program so that it can process any number of values. The input
# terminates when the user just pressed "Enter" at the prompt rather than entering a
# value

# In[49]:


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    temperatures = []

    while True:
        input_str = input("Enter a temperature in Celsius (or press Enter to finish): ")

        if not input_str:
            break

        try:
            celsius_temperature = float(input_str[:-1])
        except ValueError:
            print("Invalid input. Please enter a valid temperature followed by 'C' or press Enter to finish.")
            continue

        temperatures.append(celsius_temperature)

    if not temperatures:
        print("No temperatures entered.")
        return

    # Convert all temperatures to Fahrenheit
    fahrenheit_temperatures = [celsius_to_fahrenheit(temp) for temp in temperatures]

    # Calculate maximum, minimum, and mean
    max_temperature = max(fahrenheit_temperatures)
    min_temperature = min(fahrenheit_temperatures)
    mean_temperature = sum(fahrenheit_temperatures) / len(fahrenheit_temperatures)

    
    print(f"Maximum temperature: {max_temperature:.2f}F")
    print(f"Minimum temperature: {min_temperature:.2f}F")
    print(f"Mean temperature: {mean_temperature:.2f}F")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




