#Create a Python script that takes an input from the user and checks if it is a vowel or consonant.
n=input("eneter a string")
v="aeiouAEIOU"
if len(n)>1:
    print("enter single character")
elif n in v:
    print("vowels")
else:
    print("consonant")
    