from turtle import Turtle


FONT = ("Courier", 24, "normal")
SCORE_POSITION = (-280, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POSITION)
        self.updater()

    def updater(self):
        self.write(f"Level {self.level}", align="left", font=FONT)
    
    def lvl_up(self):
        self.level += 1
        self.clear()
        self.updater()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="CENTER", font=FONT)
