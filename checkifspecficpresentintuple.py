tuples = ((1, 2), (3, 4), (5, 6))
element = 3
if any(element in t for t in tuples):
    print(f"{element} is present in the tuple of tuples.")
else:
    print(f"{element} is not present in the tuple of tuples.")
    
# check is the number is presnt or not 
