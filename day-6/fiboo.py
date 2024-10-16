#Display Fibonacci series up to 10 terms

n=int(input("enter a numvber"))
a=0
b=1
for i in range(n):
    c=a+b
    a=b
    b=c
    print(c)