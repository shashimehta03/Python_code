s = input("enter a string ")
if len(s) < 3:
    rs = s
# elif s[-3:] == 'ing':
#      rs = s+ 'ly'
else:
     rs = s + 'ing'
print (rs)