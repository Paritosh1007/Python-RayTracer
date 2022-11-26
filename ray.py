class Ray:
    """ Ray is a unidirectional line with and origin """

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()

