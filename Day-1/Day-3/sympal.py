#Python program to check whether the string is Symmetrical or Palindrom
def strpal(s):
    return s==s[::-1]
def strsym(s):
    l=len(s)
    m=l//2
    if l%2==0:
        return s[:m]==s[m:]
    else:
        return s[:m]!=s[m:]      
s=input()
if strpal(s):
    print("palindrome")
else:
    print("not palindrome")    
if strsym(s):
    print("symmetrical")
else:
    print("not symmetrical")        