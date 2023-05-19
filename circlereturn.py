def calculate(radius):
    pi = 22/7
    area = pi * (radius ** 2)
    return area
radius = 5
area = calculate(radius)
print("The area of a circle with radius", radius, "is", area)
