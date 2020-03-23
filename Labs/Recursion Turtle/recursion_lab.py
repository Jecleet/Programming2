'''
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)

2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)


 Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

  Have fun!

'''

import turtle
import math
# set up my turtle
my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape('turtle')
my_turtle.speed(0)

# set up my screen
my_screen = turtle.Screen()
my_screen.bgcolor('white')

# draw shape using headings
my_turtle.up()
my_turtle.goto(-200, 200)
my_turtle.down()
my_turtle.setheading(270)  # face south
my_turtle.fillcolor('blue')
my_turtle.begin_fill()

def recursive_htree(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.setheading(0)
        my_turtle.forward(height)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.right(180)
        my_turtle.forward(2 * height)
        my_turtle.right(180)
        my_turtle.forward(height)
        my_turtle.left(90)
        my_turtle.forward(2 * height)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.right(180)
        my_turtle.forward(2*height)
        recursive_htree(x + height, y + height, height / 2, depth - 1)  # top bracket
        recursive_htree(x + height, y - height, height / 2, depth - 1)
        recursive_htree(x - height, y + height, height / 2, depth - 1)
        recursive_htree(x - height, y - height, height / 2, depth - 1)

#recursive_htree(0, 0, 150, 4)

my_screen.clear()


def snowflake_fractal(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + height, y) #
        my_turtle.up() #               these 3 lines of code it doesn't work but these lines don't draw anyting??
        my_turtle.goto(x, y) #
        my_turtle.down()
        my_turtle.goto(x + math.cos(math.pi/3) * height, y + math.sin(math.pi/3) * height)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + math.cos(2* math.pi / 3) * height, y + math.sin(2 * math.pi / 3) * height)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x - height, y)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x - math.cos(math.pi / 3) * height, y - math.sin(math.pi / 3) * height)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x - math.cos(2 * math.pi / 3) * height, y - math.sin(2 * math.pi / 3) * height)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + height, y)

        snowflake_fractal(x + height, y, height / 3, depth - 1)
        snowflake_fractal(x + math.cos(math.pi / 3) * height, y + math.sin(math.pi / 3) * height, height / 3, depth - 1)
        snowflake_fractal(x + math.cos(2 * math.pi / 3) * height, y + math.sin(2 * math.pi / 3) * height, height / 3, depth - 1)
        snowflake_fractal(x - height, y, height / 3, depth - 1)
        snowflake_fractal(x - math.cos(math.pi / 3) * height, y - math.sin(math.pi / 3) * height, height / 3, depth - 1)
        snowflake_fractal(x - math.cos(2 * math.pi / 3) * height, y - math.sin(2 * math.pi / 3) * height, height / 3, depth - 1)

#snowflake_fractal(0, 0, 200, 4)

my_screen.clear()

def octogon_fractal(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x - height / 4, y + height / 2)
        my_turtle.down()
        for i in range(8):
            my_turtle.forward(height)
            my_turtle.left(45)
        my_turtle.up()
        my_turtle.goto(x + height / 4, y - height / 2)
        my_turtle.down()
        my_turtle.right(180)
        for i in range(8):
            my_turtle.forward(height)
            my_turtle.left(45)
        octogon_fractal(x, y, 2 * height / 3, depth - 1)


octogon_fractal(0, 0, 150, 10)

my_screen.exitonclick()
