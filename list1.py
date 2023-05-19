
tuple = [(7,2),(4,9),(8,6)]
length = len(tuple)
inc_order = ()
for i in range(0,length):
    for j in range(0,length-i-1):
        if(tuple[j][-1] > tuple[j+1][-1]):
            temp = tuple[j]
            tuple[j] = tuple[j+1]
            tuple[j+1] = temp
print("Elements in increasing order are: ")
for i in range(len(tuple)):
    print(tuple[i])
