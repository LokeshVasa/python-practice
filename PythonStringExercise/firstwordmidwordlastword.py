'''
Create a new string made of the first, middle, and last characters of each input string
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

Given:

s1 = "America"
s2 = "Japan"
Expected Output:

AJrpan

'''
def firstmidlastword(s1,s2):
    first=s1[0]+s2[0]
    last=s1[-1]+s2[-1]
    length=len(s1)
    mid=length//2 
    length1=len(s2)
    mid2=length1//2 
    
    print(first+s1[mid]+s2[mid2]+last)



s1="America"
s2 = "Japan"
s=firstmidlastword(s1,s2)