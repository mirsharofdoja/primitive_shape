from polygon import Polygon

class Square(Polygon):
    def __init__(self,height):
        Polygon.__init__(height,height)
