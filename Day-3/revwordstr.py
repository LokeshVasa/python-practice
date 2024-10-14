#Reverse Words in a Given String in Python
n=input("enter a text")
l=[]
s=n.split()[::-1]
for i in n:
    l.append(i)
print(l)    