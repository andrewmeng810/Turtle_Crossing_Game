import turtle as t

FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color('black')
        self.goto(-280, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write('Leve: {}'.format(self.level), align='Left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Courier', 40, 'bold'))


