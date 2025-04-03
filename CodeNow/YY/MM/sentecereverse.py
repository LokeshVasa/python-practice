'''

inp:- hi lokesh 
ot:- ih hsekol

'''

def reverseofstring(inpu):
    conv=list(inpu)
    reversed_conv = conv[::-1]
    return "".join(reversed_conv)

inpu=input("enter a string:- ")
print(reverseofstring(inpu))