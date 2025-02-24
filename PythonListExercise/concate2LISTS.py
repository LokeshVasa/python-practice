'''
Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Expected output:

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
'''

list1 = ["Hello ", "take "]
list2 = ["Dear ", "Sir "]
list3=["morning ", "evening "]
#print(list1[0]+list2[0],list1[0]+list2[1], list1[1]+list2[0], list1[1]+list2[1])

'''
00
01
10
11


00 01 
10 11
'''
empty_list=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        for k in range(len(list3)):
            empty_list.append(list1[i]+list2[j]+list3[k])
print(empty_list)        
        