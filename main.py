# import colorgram
#
# colors = colorgram.extract("Hirstspotpainting.jpg", 64)
# print(colors)
# color_arr = []
# for color in colors:
#     color_arr.append(tuple(color.rgb))
# print(color_arr)

from turtle import Turtle, Screen
import random

turt = Turtle()
turt.shape("classic")
turt.pen()
turt.speed("fastest")
turt.pensize(20)
tscreen = Screen()
tscreen.screensize(1000,1000,"Black")
tscreen.colormode(255)
colour_list = [(253, 253, 252), (242, 244, 247), (241, 247, 243), (144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45), (14, 101, 109), (188, 190, 201), (11, 112, 104), (65, 66, 58)]

inc = 0
for _ in range(20):
    turt.penup()
    turt.setpos(-300, -300 + inc)
    for _ in range(20):
        turt.pendown()
        dot_colour = random.choice(colour_list)
        turt.dot(15, dot_colour)
        turt.penup()
        turt.forward(25)
    inc += 25

tscreen.exitonclick()


