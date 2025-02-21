'''
String characters balance Test
Write a program to check if two strings are balanced. For example, strings s1 and s2 are
balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.

Given:
Case 1:
s1 = "Yn"
s2 = "PYnative"
Expected Output:
True
Case 2:
s1 = "Ynf"
s2 = "PYnative"
Expected Output:
False
'''
s1= "Ynk"
s2 ="PYnative"
count=0
for i in s1:
    if i in s2:
        count+=1
        print(i)
if count == len(s1):
    print("all characters are there")
else:
    print("try again")        

