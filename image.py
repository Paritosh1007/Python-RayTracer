
class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def write_ppm(self, img_file):
        def to_byte(c):
            return round(max(min(c*255, 255), 0))

        # header of the ppm file describing its format no of pixels m x n

        img_file.write("P3 {} {}\n255\n".format(self.width, self.height))
        for row in self.pixels:
            for color in row:
                # each pixel is fetched from the buffer and written to the img_file
                img_file.write("{} {} {} ".format(to_byte(color.x), to_byte(color.y), to_byte(color.z)))



