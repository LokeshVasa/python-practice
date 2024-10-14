#Use a while loop to print the Fibonacci sequence up to the 10th term.
n=int(input("enter how many times: "))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")