from turtle import Turtle 
import turtle

class Paddle(Turtle):
    turtle.register_shape("rectangle",((0,0),(100,0),(100,20),(0,20)))
    #TODO: ask why module.staticmethod
    def __init__(self,start_coord):
        super().__init__()
        self.shape("rectangle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.setpos(start_coord)
        #TODO: ask: usually setpos is (x = 350, y = 0), but i passed in tuple this time and it still worked?
        #TODO: isnt tuple only one argument only tho? eg i pass in start_coord = (350, 0) and it still works 


    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(x = self.xcor(), y = new_y)
        #TODO:ask why dont need return here again!!???

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(x = self.xcor(),y = new_y)
