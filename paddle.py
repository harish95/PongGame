from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,type='right'):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        if type == 'right':
            self.goto(350,0)
        elif type == 'left':
            self.goto(-350,0)

    def go_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)

