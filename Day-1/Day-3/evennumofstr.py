#Python program to print even length words in a string
def evenlen(s):
    emp=''
    for i in range(len(s)):
        if i%2==0:
            emp+=s[i]
    return emp

    
s=input("enter a text")
print(evenlen(s))    