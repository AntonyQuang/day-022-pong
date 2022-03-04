from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, POSITION):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(POSITION)
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)