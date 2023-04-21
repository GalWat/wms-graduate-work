import drawsvg as draw
from enum import IntEnum


class Orientation(IntEnum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3


class Drawer:
    def __init__(self, block_size: int, w_count: int, h_count: int, pixel_scale=1):
        self.d = draw.Drawing(block_size * w_count, block_size * h_count)
        self.d.set_pixel_scale(pixel_scale)
        self.block_size = block_size
        self.w_count = w_count
        self.h_count = h_count

    def draw(self, racks: dict):
        """racks: {(x, y): orientation}"""
        rack_elem = Rack()
        empty_elem = Empty()

        for x in range(self.w_count):
            for y in range(self.h_count):
                empty_elem.draw(self.d, x * self.block_size, y * self.block_size)
                if (x, y) in racks:
                    orientation = Orientation(racks[(x, y)])
                    rack_elem.draw(self.d, x * self.block_size, y * self.block_size, orientation)

        return self.d


class Element:
    def __init__(self):
        self.group = draw.Group()

    def draw(self, drawing: draw.Drawing, x: int, y: int, orientation: Orientation = Orientation.LEFT):
        drawing.append(draw.Use(self.group, x, y, transform=f'rotate({orientation * 90} {x + 12.5} {y + 12.5})'))


class Rack(Element):
    def __init__(self):
        super().__init__()
        self.group.append(draw.Rectangle(8, 1, 15, 23, fill='linen', stroke='none'))
        self.group.append(draw.Lines(5, 1, 23, 1, 23, 24, 5, 24, stroke='black', fill='none'))
        self.group.append(draw.Line(8, 3, 8, 22, stroke='black', fill='none', stroke_width=0.3))


class Empty(Element):
    def __init__(self):
        super().__init__()
        self.group.append(draw.Rectangle(0.5, 0.5, 24, 24, fill='whitesmoke', stroke='none'))

