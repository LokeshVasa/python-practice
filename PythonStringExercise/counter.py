'''

 Count all letters, digits, and special symbols from a given string
Given:

str1 = "P@#yn26at^&i5ve"
Expected Outcome:

Total counts of chars, digits, and symbols 

Chars = 8 
Digits = 3 
Symbol = 4


'''

str1 = "P@#yn26at^&i5ve"
chars =[]
Digits=[]
symbol=[]
for i in str1:
    if i.isalpha():
        chars.append(i)
    elif i.isdigit():
        Digits.append(i)
    else:
        symbol.append(i)
print(Digits)
print(chars)
print(symbol)                