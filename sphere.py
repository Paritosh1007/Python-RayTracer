from math import sqrt


class Sphere:
    """ Sphere is the only shape implemented. It has position, radius & material"""

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray):
        """ Check if ray intersects with the sphere. Returns distance if it intersects & None if it doesn't"""
        sphere_to_ray = ray.origin - self.center
        # a = 1
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 * c

        if discriminant > 0:
            distance = (-b - sqrt(discriminant)) / 2
            if distance > 0:
                return distance

        return None
