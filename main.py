from image import Image
from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine
from light import Light
from material import Material

def main():
    # WIDTH & HEIGHT ARE CONSTANT SO THEY ARE WRITTEN IN UPPER CASE
    WIDTH = 320
    HEIGHT = 200
    camera = Vector(0, 0, -1)
    image = Image(WIDTH, HEIGHT)
    # sphere with coordinates, radius
    objects = [Sphere(Point(0, 0, 0), 0.3, Material(Color.from_hex("#FF0000")))]
    lights = [Light(Point(1.5, -0.5, -10.0), Color.from_hex("#FFFFFF"))]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)
    # writing the buffer to the file called test.ppm which is stored
    # in a variable called img_file
    with open("test.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == '__main__':
    main()
