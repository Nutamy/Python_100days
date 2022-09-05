from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 275)
        self.high_score = 0
        self.var_score = 0
        self.str_score = f"Score: {self.var_score}"
        self.refresh()

    def refresh(self):
        self.clear()
        self.str_score = f"Score: {self.var_score}"
        self.write(self.str_score, move=False, align=ALIGN, font=FONT)
        self.var_score += 1

    def reset(self):
        if self.var_score > self.high_score:
            self.high_score = self.var_score
        self.var_score = 0
        self

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", move=False, align=ALIGN, font=FONT)

