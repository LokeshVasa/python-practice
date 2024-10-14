'''
Implement a Python program that simulates a basic ATM. The user should be able to check their
balance, deposit money, and withdraw money with condition checks.
'''
print("              welcome to ATM        ")
print("1.check balance")
print("2.deposit money")
print("withdraw money")
n=int(input("enter u r choice"))
money=45000
c=0
d=0
w=0
if n==2:
    x=int(input("enter how much money do you want to deposit="))
    d=x
    print("sucessfuly depposited",d)
    print("your current balance is:",d+money)
    print("do you want to withdraw")
    print("yes")
    print("no")
    q=input("enter ur choice")
    if q=='yes':
        e=int(input("how much do you want to withdraw"))
        print(d-e)

 


