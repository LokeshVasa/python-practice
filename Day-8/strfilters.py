# Count all letters, digits, and special symbols from a given string
#isalpha()	Returns True if all characters in the string are in the alphabet
#isalnum()	Returns True if all characters in the string are alphanumeric



def string_separation(str1):
    digits=""
    characterss=""
    symbols=""
    for i in str1:
        if i.isalpha():
            characterss+=i
        elif i.isalnum():
            digits+=i
        else:
            symbols+=i
    print("characters=",len(characterss))
    print("digits=",len(digits)) 
    print("symbols=",len(symbols))                
str1="jpgij450e)(t^tb$iu@b0"
result=string_separation(str1)

