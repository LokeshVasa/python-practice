#Create a string made of the middle three characters

'''
in;-JhonDipPeta
ot:-Dip

in;-"JaSonAy
ot;-son
'''

val="JhonDipPeta"
length=len(val)
mid=length//2
print(val[mid-1]+val[mid]+val[mid+1])


val="JaSonAy"
length=len(val)
mid=length//2
print(val[mid-1]+val[mid]+val[mid+1])