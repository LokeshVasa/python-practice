'''
Replace each special symbol with # in the following string
Given:

str1 = '/*Jon is @developer & musician!!'
Expected Output:

##Jon is #developer # musician##


'''

#Syntax
#string.replace(oldvalue, newvalue, count)


str1:str= '/*Jon is @developer & musician!!'
empty_string=''
for i in str1:
    if i==' ':
        empty_string+=i
    elif not i.isdigit() and not i.isalpha():
        empty_string+='#'
    else:
        empty_string+=i    
print(empty_string)