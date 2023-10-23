class VisColor:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def as_tuple(self):
        return self.r, self.g, self.b


class VisColors:
    MAGENTA = VisColor(255, 0, 255).as_tuple()
    FOREST_GREEN = VisColor(74, 103, 65).as_tuple()
    GRAY = VisColor(128, 128, 128).as_tuple()
    YELLOW = VisColor(255, 255, 0).as_tuple()
    BROWN = VisColor(165, 92, 42).as_tuple()
    PINK = VisColor(255, 128, 128).as_tuple()
    PURPLE = VisColor(106, 50, 159).as_tuple()
    RED = VisColor(255, 0, 0).as_tuple()
    DARK_BLUE = VisColor(22, 83, 126).as_tuple()
    SKY_BLUE = VisColor(69, 212, 255).as_tuple()
    GOLD = VisColor(255, 208, 63).as_tuple()
    BLUE = VisColor(0, 0, 255).as_tuple()


def contrast_color(b:tuple[int, int, int]):
    return (
        255-(b[0]//2),
        255-(b[1]//2),
        255-(b[2]//2))
