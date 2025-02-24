'''
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
Expected output:

["Mike", "Emma", "Kelly", "Brad"]

'''
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
empty_list=[]
for i in list1:
    if i:
        empty_list.append(i)
print(empty_list)        