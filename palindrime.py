num = int(input("Enter a Number:"))  
temp = num  
rev = 0  
while(num > 0):  
    dig = num % 10  
    rev = rev * 10 + dig  
    num = num // 10  
if(temp == rev):  
    print(" palindrome number!")  
else:  
    print(" not a palindrome number!")