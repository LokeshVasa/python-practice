'''
Write a Python program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the following number
If the number is greater than 500, then stop the loop
Given:

numbers = [12, 75, 150, 180, 145, 525, 50]
'''
numbers = [12, 75, 150, 180, 145, 525, 50]
l=[]
for i in numbers:
    if i>500:break
    elif i>=150:continue
    elif i%5==0:
        l.append(i)
print(l)        
        