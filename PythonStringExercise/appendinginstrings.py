'''

Append new string in the middle of a given string
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

Given:

s1 = "Ault"
s2 = "Kelly"
Expected Output:

AuKellylt



'''

s1="Ault"
s2="Kelly"
print(s1[0:2]+s2[0:5]+s1[2:4])