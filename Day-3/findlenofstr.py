#Find length of a string in python
def lengthofstr(s):
    c=0
    for i in s:
        c+=1
    return c
s=input("enter a text")
print(lengthofstr(s))