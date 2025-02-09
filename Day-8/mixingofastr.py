#Create a mixed String using the following rules
'''
i/p:-lokesh
i/p:-chandra
o/p:-laknhc
'''
def mixed_string(str1, str2):
    first=str1[0]+str2[-1]
    middle=len(str1)//2
    middle2=len(str2)//2
    last=str1[-1]+str2[0]
    mid1=str1[middle]+str2[middle2]
    return first+mid1+last

str1="lokesh"
str2="chandra"
print(mixed_string(str1,str2))