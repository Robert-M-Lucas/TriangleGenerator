import random
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.connections = []

    def random_offset(self, max_magnitude, min_magnitude=0):
        # self.random_x(max_magnitude)
        # self.random_y(max_magnitude)
        # return

        mag = (random.random() * (max_magnitude - min_magnitude)) + min_magnitude
        angle = (2 * math.pi * random.random()) - math.pi
        if 0 <= angle < 90:
            x, y = mag * math.cos(angle), mag * math.sin(angle)
        elif 90 <= angle <= 180:
            angle = 180 - angle
            x, y = mag * math.cos(angle), -mag * math.sin(angle)
        elif 0 > angle > -90:
            angle = -angle
            x, y = -mag * math.cos(angle), - mag * math.sin(angle)
        elif -90 >= angle >= -180:
            angle = 180 + angle
            x, y = -mag * math.cos(angle), -mag * math.sin(angle)
        self.x, self.y = self.x + x, self.y + y

    def random_x(self, magnitude):
        self.x += (random.random() * magnitude * 2) - magnitude

    def random_y(self, magnitude):
        self.y += (random.random() * magnitude * 2) - magnitude


def generate_points(size, cells, randomness, min_randomness=0) -> [[Point]]:
    points: [[Point]] = []

    for x in range(cells[0]):
        points.append([])
        backwards = False
        for y in range(cells[1]):
            x2, y2 = int(((size[0] - 1) / (cells[0] - 1)) * x), int(
                ((size[1] - 1) / (cells[1] - 1)) * y)
            points[x].append(Point(x2, y2))

            """
            if x != cells[0] - 1:
                points[x][y].connections.append([x + 1, y])
            if y != cells[1] - 1:
                points[x][y].connections.append([x, y + 1])

            if backwards and x < (cells[0] - 1):
                points[x][y].connections.append([x + 1, y - 1])

            backwards = random.choice([True, False])

            if not backwards and x < (cells[0] - 1) and y < (cells[1] - 1):
                points[x][y].connections.append([x + 1, y + 1])

            try:
                if x > 0 and y > 0 and [x, y] in points[x - 1][y - 1].connections:
                    points[x][y].connections.append([x - 1, y - 1])
            except IndexError:
                pass

            try:
                if y > 0 and [x, y] in points[x + 1][y - 1].connections:
                    points[x][y].connections.append([x + 1, y - 1])
            except IndexError:
                pass
            """

            if not (x == 0 or y == 0 or x == cells[0] - 1 or y == cells[1] - 1):
                points[x][y].random_offset(randomness, min_randomness)
            elif x != 0 and x != cells[0] - 1 and (y == 0 or y == cells[1] - 1):
                points[x][y].random_x(randomness)
            elif y != 0 and y != cells[1] - 1 and (x == 0 or x == cells[0] - 1):
                points[x][y].random_y(randomness)

    return points
