a="hello"
b=len(a)
print(b)
print(a[2])
for i in range (0,b):
    print(a[i])
for i in range (0,b):
    if(a[i]=='o'):
        print(i)
        break
    else:
        print("NO")
        break
print(a.replace("e","s"))
b="coder"
#print(capitalize(b))
s1=slice(3)
s2=slice(3,5)
s3=slice(3,5,2)
print(b[s1])
print(b[s2])
print(b[s3])
print(min(a))
print(max(a))
print(ord('&'))
print(chr(30))
z='s'+b
print(z)
print(a==b)
print(a>b)
print(a<b)
print(a!=b)




