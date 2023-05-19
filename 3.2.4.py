class Circleconc():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

obj = Circleconc(8)
print(obj.area())
print(obj.perimeter())
