n=int(input("enter a number :"))
s=str(n)
l=[]
for i in s:
    b=int(i)**3
    l.append(b)
#print(sum(l))
if n==sum(l):
    print("armstrong")
else:
    print("not a armstrong")    