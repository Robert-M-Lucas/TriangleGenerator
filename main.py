import random
import turtle
from points import generate_points, Point
from color import Color, get_balanced_color
import math

size = (1000, 1000)
cells = (20, 20)
randomness = 17  # Random offset of points
min_randomness = 8

# Top-left,    Top-right
# Bottom-left, Bottom-right
colors = [None, Color(130, 161, 255),
          Color(255, 0, 144), None]

color_variance = 25  # Randomness of color

points = generate_points(size, cells, randomness, min_randomness)

turtle.screensize(canvwidth=size[0], canvheight=size[1])
turtle.colormode(255)
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.tracer(0, 0)


def translate(x_val, y_val):
    return x_val - size[0] / 2, y_val - size[1] / 2


def get_color(point: Point):
    return random.choice([(get_balanced_color(colors, point.x, point.y, size) + (
            Color.Grey(color_variance) * random.random())).get_tuple(),

          (get_balanced_color(colors, point.x, point.y, size) - (
                  Color.Grey(color_variance) * random.random())).get_tuple(),
          ])


# Draw
for x, row in enumerate(points[:-1]):
    for y, p in enumerate(row[:-1]):

        backwards = random.choice([True, False])
        t.color(get_color(p))

        if not backwards:
            t.penup()
            t.goto(translate(p.x, p.y))
            t.pendown()
            t.begin_fill()
            t.goto(translate(points[x + 1][y].x, points[x + 1][y].y))
            t.goto(translate(points[x + 1][y + 1].x, points[x + 1][y + 1].y))
            t.goto(translate(p.x, p.y))
            t.end_fill()

            t.color(get_color(p))

            t.penup()
            t.pendown()
            t.begin_fill()
            t.goto(translate(points[x + 1][y + 1].x, points[x + 1][y + 1].y))
            t.goto(translate(points[x][y + 1].x, points[x][y + 1].y))
            t.goto(translate(p.x, p.y))
            t.end_fill()
            t.penup()
        else:
            t.penup()
            t.goto(translate(p.x, p.y))
            t.pendown()
            t.begin_fill()
            t.goto(translate(points[x + 1][y].x, points[x + 1][y].y))
            t.goto(translate(points[x][y + 1].x, points[x][y + 1].y))
            t.goto(translate(p.x, p.y))
            t.end_fill()

            t.color(get_color(p))

            t.penup()
            t.goto(translate(points[x][y + 1].x, points[x][y + 1].y))
            t.pendown()
            t.begin_fill()
            t.goto(translate(points[x + 1][y].x, points[x + 1][y].y))
            t.goto(translate(points[x + 1][y + 1].x, points[x + 1][y + 1].y))
            t.goto(translate(points[x][y + 1].x, points[x][y + 1].y))
            t.end_fill()
            t.penup()
turtle.update()

turtle.getscreen().getcanvas().postscript(file="main.eps", width=size[0], height=size[1])  # Saving

turtle.mainloop()
