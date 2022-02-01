from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
SCORE_POSITION = (0, 265)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("100 days of python\\Day 24\\score.txt") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.goto(SCORE_POSITION)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)


    def score_change(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("100 days of python\\Day 24\\score.txt", mode="w") as f:
                f.write(f"{self.high_score}")
        self.score = 0

        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)