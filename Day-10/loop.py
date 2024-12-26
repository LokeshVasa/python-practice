# 9 > 1, 3, 9 # not prime
# 10> 1, 2, 5, 10 # not prime
# 20> 1, 2, 4, 5, 10, 20  # not prime
# factors more than 1 and itself

# 23> 1, 23  
# 17> 1, 17


# prime
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37 .....

def isPrime(n)->bool:
    if n<=1:
        return False
    
    for i in range(2, n):
        if n%i==0:
            return False
    return True
        
# n= 1
# print(isPrime(n))

for i in range(1, 101):
    if isPrime(i):
        print(i)
        
