num = int(input("Enter 3-digit number : ")) 
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit * digit * digit
    temp = temp//10
 
if sum==num:
    print(' Armstrong number')
else:
    print('not an Armstrong number')