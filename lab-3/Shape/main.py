from shape import Circle, Square, Triangle
from renderer import VectorRenderer, RasterRenderer

def main():
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    circle = Circle(vector_renderer)
    square = Square(raster_renderer)
    triangle = Triangle(vector_renderer)

    circle.draw()
    square.draw()
    triangle.draw()

if __name__ == "__main__":
    main()
