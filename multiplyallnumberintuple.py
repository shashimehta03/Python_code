def prod(val) :
    res = 1
    for ele in val:
        res *= ele
    return res 
test_tup = (7, 8, 9, 1, 10, 7)
print("The original tuple is : " + str(test_tup))
res = prod(list(test_tup))
 
print("The product of tuple elements are : " + str(res))

# multiplig an tuple 