#Append new string in the middle of a given string

def midstr(n,c):
    m=int(len(n)/2)
    return n[0:m]+c+n[m:len(n)]
    
n="lokesh"
c="chandra"
print(midstr(n,c))


#o/p:-lokchandraesh
