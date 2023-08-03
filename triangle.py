from polygon import Polygon

class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getPerimeter(self):
        return self.a+self.b+self.c
    def getArea(self):
        p=self.getPerimeter()/2
        return (p*(p-self.a)*(p*self.b)*(self.c))**0.5