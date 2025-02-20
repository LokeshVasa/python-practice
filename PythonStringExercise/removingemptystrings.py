'''
 Remove empty strings from a list of strings
Given:

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
Expected Output:

Original list of sting
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']
    
    
    
'''
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
empty_list=[]
for i in str_list:
    if i:
        empty_list.append(i)
print(empty_list)        
