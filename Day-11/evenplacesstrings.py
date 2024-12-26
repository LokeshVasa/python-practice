"""
Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

"""
n=input("enter a string: ")
x=list(n)
for i in x[0::2]:
    print(i,end=" ")

#using list slicing
