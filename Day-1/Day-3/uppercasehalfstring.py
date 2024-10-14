#Python – Uppercase Half String


s=input("enter a string")
m=len(s)//2
sf=''
for i in range(len(s)):
    if i<=m:
        sf+=s[i].upper()
print(sf)        
