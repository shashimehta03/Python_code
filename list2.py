#list = ['Red','green','blue','yellow','violet','pink'] 
list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
length = len(list)
for i in range(0,length):
    if i not in (0,4,5):
        print(list[i])
