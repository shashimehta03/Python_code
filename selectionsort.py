def selectionSort(array, size):
    	
	for s in range(size):
		min_idx = s
		
		for i in range(s + 1, size):
			if array[i] < array[min_idx]:
				min_idx = i
		(array[s], array[min_idx]) = (array[min_idx], array[s])
data = [ 4,9,8,7,6 ]
size = len(data)
selectionSort(data, size)

print('Sorted Array in Ascending Order:')
print(data)