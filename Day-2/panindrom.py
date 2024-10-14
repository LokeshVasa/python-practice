#Write a Python program that checks whether a given string is a palindrome (reads the same forwards and backwards).
n=input("enter ur string:-")
x=n
if n==x[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
