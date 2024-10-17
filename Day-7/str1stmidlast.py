#Write a program to create a new string made of an input string’s first, middle, and last character.
#i/p:-lokesh
#o/p:-lkh
n=input("enter a character :-")
l=len(n)
f=n[0]
ls=n[-1]
if l % 2 == 0:
    m = n[l // 2 - 1]  
else:
    m= n[l // 2]
newstr=f+m+ls
print(newstr)