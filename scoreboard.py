from turtle import Turtle

class Scoreboard(Turtle):
    def __int__(self):
        super().__init__()
        self.write(arg="My Score", move=False, align="center", font=("times new roman", 10, "bold"))
