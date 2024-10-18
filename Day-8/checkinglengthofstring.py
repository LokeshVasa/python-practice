'''
String characters balance Test
Write a program to check if two strings are balanced. For example, 
strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
 The character’s position doesn’t matter.
'''

def checinglength_of_string(str1,str2):
    if len(str1)==len(str2):
        return True
    else:
        return False
str1="lokesh"
str2="arvind"
print(checinglength_of_string(str1,str2))