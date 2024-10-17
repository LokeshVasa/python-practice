
def order_lower_upper(s):
     lower=""
     upper=""
     for i in s:
          if i.islower():
               lower+=i
          else:
               upper+=i 

     return lower+upper                 

s="HIpython"
print(order_lower_upper(s))