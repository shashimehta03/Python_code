class Rectangleconc():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

obj= Rectangleconc(12, 10)
print(obj.rectangle_area())
