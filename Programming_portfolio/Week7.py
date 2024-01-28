#!/usr/bin/env python
# coding: utf-8

# Write and test a function that takes a string as a parameter and returns a sorted list
# of all the unique letters used in the string. So, if the string is cheese, the list
# returned should be ['c', 'e', 'h', 's'].

# In[26]:


def cheese(string):
    sorted_letters = sorted(set(string))
    return sorted_letters
result = cheese("nepala")
print(result)


# Write and test three functions that each take two words (strings) as parameters and
# return sorted lists (as defined above) representing respectively:
# Letters that appear in at least one of the two words.
# Letters that appear in both words.
# Letters that appear in either word, but not in both.
# Hint: These could all be done programmatically, but consider carefully what topic we
# have been discussing this week! Each function can be exactly one line

# In[34]:


def either(word1, word2):
    return sorted(set(word1) or set(word2))

def both(word1, word2):
    return sorted(set(word1) and set(word2))

def either_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))
word1 = "hii"
word2 = "there"

result1 = either(word1, word2)
result2 = both(word1, word2)
result3 = either_not_both(word1, word2)

print("Letters in either word:", result1)
print("Letters in both words:", result2)
print("Letters in either, but not both:", result3)



# Write a program that manages a list of countries and their capital cities. It should
# prompt the user to enter the name of a country. If the program already "knows"
# the name of the capital city, it should display it. Otherwise it should ask the user to
# enter it. This should carry on until the user terminates the program (how this
# happens is up to you).
# Note: A good solution to this task will be able to cope with the country being entered
# variously as, for example, "Wales", "wales", "WALES" and so on

# In[35]:


countries_capitals = {}
def get_country():
    return input("Enter the name of a country (or 'exit' to terminate): ").strip().title()

def main():
    while True:
        country = get_country()

        if country.lower() == 'exit':
            print("Terminating the program.")
            break

        capital = countries_capitals.get(country)

        if capital:
            print(f"The capital city of {country} is {capital}.")
        else:
            new_capital = input(f"The capital city of {country} is not known. Enter it: ").strip().title()
            countries_capitals[country] = new_capital
            print(f"Capital city of {country} ({new_capital}) has been added to the list.")

if __name__ == "__main__":
    main()


# One approach to analysing some encrypted data where a substitution is suspected
# is frequency analysis. A count of the different symbols in the message can be used
# to identify the language used, and sometimes some of the letters. In English, the
# most common letter is "e", and so the symbol representing "e" should appear most
# in the encrypted text.
# Write a program that processes a string representing a message and reports the six
# most common letters, along with the number of times they appear. Case should
# not matter, so "E" and "e" are considered the same.
# Hint: There are many ways to do this. It is obviously a dictionary, but we will want
# zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
# best to ignore that initially, and then check the usual resources for the runes.

# In[36]:


def frequency(message):
    letter_counts = {}
    for char in message:
        if char.isalpha():
            char_lower = char.lower()
            letter_counts[char_lower] = letter_counts.get(char_lower, 0) + 1
    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)[:6]
    print("Most used:")
    for letter, count in sorted_counts:
        print(f"{letter}: {count}")
message = "We study bachelor of computer science in leeds beckett."
frequency(message)


# In[ ]:




