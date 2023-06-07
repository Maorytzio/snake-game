from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data_file:
            self.high_score = int(data_file.read())

        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increment(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align=ALIGNMENT,
                   font=('Arial', 18, 'normal'))

    def reset_game(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data_file:
                data_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.hideturtle()
        self.home()
        self.color("white")
        self.write("Game Over", False, align=ALIGNMENT, font=('Arial', 28, 'normal'))
