class Shape():

    def __init__(self):
        print("I am in init")

    def draw_shape(self):
        pass
    
    def set_color(self):
        pass

class Circle(Shape):
    def draw_shape(self):
        print("Draw Circle")

c = Circle()
c.draw_shape()
c.set_color()
