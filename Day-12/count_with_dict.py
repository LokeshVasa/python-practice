s= "Lokesh chandra thukkugudem"

d= {}

for c in s:
    if not c in d.keys():
        d[c]= 1
    elif c in d.keys():
        d[c]+=1
print(d)