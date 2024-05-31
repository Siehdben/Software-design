class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def draw(self):
        self.renderer.render_circle()

class Square(Shape):
    def draw(self):
        self.renderer.render_square()

class Triangle(Shape):
    def draw(self):
        self.renderer.render_triangle()
