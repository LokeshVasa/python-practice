#Calculate the sum and average of the digits present in a string
'''
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

Given:

str1 = "PYnative29@#8496"
Expected Outcome:

Sum is: 38 Average is  6.333333333333333

'''
def sum_and_avgrage(str1):
    digitss=[]
    for i in str1:
        if i.isdigit():
            digitss.append(int(i))
    summ=sum(digitss)
    avg=sum(digitss)/len(digitss)
    return summ,avg             

str1 = "PYnative29@#8496"
summ,avg=sum_and_avgrage(str1)
print(f"the sum is {summ} and the avgrage is {avg}")



