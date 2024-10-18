'''
String characters balance Test
Write a program to check if two strings are balanced. For example, 
strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
 The character’s position doesn’t matter.
'''

def balancing_of_string(str1,str2):
    #s=""
    for i in str1:
        if i in str2:
            return True
        else:
            return False    

str1="pug"
str2 ="PYnative"
#str2="lokesh"
print(balancing_of_string(str1,str2))