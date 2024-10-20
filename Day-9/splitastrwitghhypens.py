#3: Split a string on hyphens
#Write a program to split a given string on hyphens and display each substring.

def spliting_of_string(str1):
    s=""
    str2=""
    for i in str1:
        s=str1.split("-")
    return s    

str1 = "Emma-is-a-data-scientist"
print(spliting_of_string(str1))
