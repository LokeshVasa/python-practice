'''Find all occurrences of a substring in a given string by ignoring the case
Write a program to find all occurrences of “USA” in a given string ignoring the case.

Given:

str1 = "Welcome to USA. usa awesome, isn't it?"
Expected Outcome: The USA count is: 2'''

from inspect import stack
import queue


def occurences_of_string(str1):

    return  str1.lower().upper().count("USA")

str1 = "Welcome to USA. usa awesome, isn't it?"
print(occurences_of_string(str1))
str
int
stack
queue