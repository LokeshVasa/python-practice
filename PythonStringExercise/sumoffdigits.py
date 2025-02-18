'''
Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

Given:

str1 = "PYnative29@#8496"
Expected Outcome:

Sum is: 38 Average is  6.333333333333333

'''
str1 = "PYnative29@#8496"
digits=[]
count=0
for i in str1:
    if i.isdigit():
        digits.append(int(i))
        count+=1     
print("sum is:",sum(digits))
print("average is:",sum(digits)/count)