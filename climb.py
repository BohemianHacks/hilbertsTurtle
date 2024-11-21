import turtle

def hilbert_curve(level, angle=0):
    if level == 0:
        return ""
    
    result = ""
    
    # Rotate the direction
    angle += 90 * level % 4

    # Recursively generate the four quadrants
    result += hilbert_curve(level - 1, angle)
    result += "F"
    result += hilbert_curve(level - 1, angle + 90)
    result += "F"
    result += hilbert_curve(level - 1, angle + 180)
    result += "F"
    result += hilbert_curve(level - 1, angle + 270)

    return result

def draw_hilbert(level, angle=0, size=100):
    if level == 0:
        return

    turtle.right(angle)
    turtle.forward(size)

    draw_hilbert(level - 1, angle - 90, size / 2)
    turtle.forward(size)
    draw_hilbert(level - 1, angle, size / 2)
    turtle.forward(size)
    draw_hilbert(level - 1, angle + 90, size / 2)
    turtle.forward(size)
    draw_hilbert(level - 1, angle + 180, size / 2)

# Set up the turtle graphics
turtle.speed(0)
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()

# Draw the Hilbert curve
level = 5
size = 10
draw_hilbert(level, size=size)

turtle.done()
