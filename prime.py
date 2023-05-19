a=int(input("enter first number"))
b=int(input("enter second number"))
for val in range(a, b):
  if val > 1:
    for i in range(2, val):
      if (val % i) == 0:
        break
    else:
      print(val, end=" ")