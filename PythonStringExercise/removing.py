'''
Remove special symbols / punctuation from a string
Given:

str1 = "/*Jon is @developer & musician"
Expected Output:

"Jon is developer musician"
'''
str1 = "/*Jon is @developer & musician"
new_string=''
for i in str1:
    if i==' ':
        new_string+=i
    elif i.isalpha():
        new_string+=i
print(new_string)
