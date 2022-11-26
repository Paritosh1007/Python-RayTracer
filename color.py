from vector import Vector


class Color(Vector):
    """ stores color as RGB triplet. An alise for vector"""

    @classmethod
    def from_hex(cls, hexcolor="#000000"):
        x = int(hexcolor[1:3], 16) / 255
        y = int(hexcolor[3:5], 16) / 255
        z = int(hexcolor[5:7], 16) / 255
        return cls(x, y, z)
