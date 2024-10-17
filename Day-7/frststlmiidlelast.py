# Create a new string made of the first, middle, and last characters of each input string
def combine_first_middle_last(str1,str2):
    midstr1=int(len(str1)/2)
    midstr2=int(len(str2)/2)
    finalstring=""
    finalstring+=str1[0]+str2[0]
    finalstring+=str1[midstr1]+str2[midstr2]
    finalstring+=str1[-1]+str2[-1]
    return finalstring





str1="lokesh"
str2="chandra"
print(combine_first_middle_last(str1,str2))