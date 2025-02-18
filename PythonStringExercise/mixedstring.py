'''
Create a mixed String using the following rules
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

Given:

s1 = "Abc"
s2 = "Xyz"
Expected Output:

AzbycX

'''

s1 = "Abc"
s2 = "Xyz"
length=len(s1)
mid=length//2
length1=len(s2)
mid1=length1//2
print(s1[0]+s2[0]+s1[mid]+s2[mid1]+s1[-1]+s2[-1])