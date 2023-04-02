from turtle import Turtle,Screen,colormode
import random

colormode(255)
color_list = [(57, 106, 148), (224, 200, 110), (133, 85, 59), (222, 141, 65), (195, 145, 171), (234, 225, 203), (144, 179, 203), (224, 233, 230), (138, 82, 106), (209, 91, 68), (134, 182, 136), (187, 79, 121), (69, 104, 89), (236, 222, 230), (65, 155, 89), (133, 133, 75), (49, 155, 194), (183, 192, 201), (213, 178, 191)]
timmy = Turtle()
timmy.hideturtle()
timmy.penup()
timmy.speed("fastest")
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_dots = 100


for dot_count in range(1,number_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = Screen()
screen.exitonclick()