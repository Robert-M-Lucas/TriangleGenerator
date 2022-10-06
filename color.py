import math
from typing import *


class Color:
    def __init__(self, r: int, g: int, b: int):
        self.r: int = color_clamp(int(r))
        self.g: int = color_clamp(int(g))
        self.b: int = color_clamp(int(b))

    def get_tuple(self) -> Tuple[int, int, int]:
        return self.r, self.g, self.b

    @staticmethod
    def Grey(greyness: int = 123):
        return Color(greyness, greyness, greyness)

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __sub__(self, other):
        return Color(self.r - other.r, self.g - other.g, self.b - other.b)

    def __mul__(self, other):
        return Color(int(self.r * other), int(self.g * other), int(self.b * other))

    def __str__(self):
        return f"Color: [r:{self.r}, g:{self.g}, b:{self.b}]"


def color_clamp(num):
    return max(min(num, 255), 0)


def get_balanced_color(colors, x, y, size) -> Color:
    max_dist = math.sqrt(size[0] ** 2 + size[1] ** 2)

    influence = [0, 0, 0, 0]

    dist = math.sqrt((x**2) + (y**2))
    influence[0] = 1 - (dist / max_dist)

    dist = math.sqrt(((size[0] - x) - 1) ** 2 + y ** 2)
    influence[1] = 1 - (dist / max_dist)

    dist = math.sqrt(x ** 2 + ((size[1] - y) - 1) ** 2)
    influence[2] = 1 - (dist / max_dist)

    dist = math.sqrt(((size[0] - x) - 1) ** 2 + ((size[1] - y) - 1) ** 2)
    influence[3] = 1 - (dist / max_dist)

    for i, c in enumerate(colors):
        if c is None:
            influence[i] = 0

    normalisation_factor = 1 / sum(influence)
    for x in range(len(influence)):
        influence[x] *= normalisation_factor

    color = Color(0, 0, 0)
    for i, c in enumerate(colors):
        if c is not None:
            color += c * influence[i]

    return color
