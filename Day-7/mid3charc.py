#Create a string made of the middle three characters

def midofword(n):
    m=int(len(n)/2)
    return n[m-1:m+2]
n=input("enter u r string:-")
print(midofword(n))