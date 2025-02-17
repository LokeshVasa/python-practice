'''
Input: khokho
Output: 
The entered string is symmetrical
The entered string is not palindrome

Input:amaama
Output:
The entered string is symmetrical
The entered string is palindrome'''


def symetricalandpalindrome(inputt):
    length=len(inputt)
    mid=length/2
    if length%2==0:
        return inputt[:mid]==inputt[mid:]
    else:
        return False

    
        

inputt=input(":=")
print(symetricalandpalindrome(inputt))