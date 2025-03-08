'''
7
1,3,4,6,7,5,2

8
8,7,6,5,4,3,2,1

'''

n1=int(input("enter how many many :"))
list1=[]
for i in range(n1):
    x=int(input("enter values"))
    list1.append(x)
print(list1)    


n2=int(input("enter how many many :"))
list2=[]
for i in range(n2):
    y=int(input("enter values"))
    list2.append(y)
print(list2)    


for element in list2:
    if element not in list1:
        print(element)
print()   :