""""
Remove first n characters from a string
Write a Python code to remove characters from a string from 0 to n and return a new string.

"""
def remove_chars(word,rem):
    x=word[rem: ]
    return x
word=input(" enter a string: ")
rem=int(input("enter how digits you want to remove: "))
print(remove_chars(word,rem))