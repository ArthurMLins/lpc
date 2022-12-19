import turtle


class Paddle(turtle.Turtle):

    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(0.2, 3)
        self.up()
        self.color('white')
        self.goto(0, -250)

    def move_right(self):
        if self.xcor() <= 350:
            self.goto(self.xcor() + 60, self.ycor())

    def move_left(self):
        if self.xcor() >= -350:
            self.goto(self.xcor() - 60, self.ycor())


class Ball(turtle.Turtle):
    def __init__(self, paddle, block_list):
        super().__init__(shape='circle')
        self.up()
        self.color('white')
        self.dx, self.dy = 4, 5
        self.paddle = paddle
        self.block_list = block_list

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

        # Border bounce
        if self.xcor() <= -220 or self.xcor() >= 190:
            self.dx *= -1
        if self.ycor() >= 400:
            self.dy *= -1
        if self.ycor() < -400:
            self.goto(0, 0)

        # Paddle bounce
        if (-250 <= self.ycor() <= -240) and (
                self.paddle.xcor() - 60 < self.xcor() < self.paddle.xcor() + 60) and self.dy < 0:
            self.dy *= -1


class Block(turtle.Turtle):
    def __init__(self, xpos, ypos):
        super().__init__(shape='square')
        self.up()
        self.shapesize(0.5, 1.3),
        self.goto(xpos, ypos)
        self.color('purple')



class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.color('white')
        self.up()
        self.hideturtle()
        self.goto(200, -200)


class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(450, 800)
        self.screen.bgcolor('black')
        self.screen.title('Breakout')
        self.screen.tracer(0)
        self.screen.listen()

        self.pen = Scoreboard()

    def new_game(self):

        self.x_list = [-200, -170, -140, -110, -80, -50, -20, 10, 40, 70, 100, 130, 160, 190]
        self.y_list = [370, 350, 330, 310, 290, 270]
        self.block_list = []

        self.paddle = Paddle()
        self.ball = Ball(self.paddle, self.block_list)
        self.pen.clear()

        for i in self.x_list:
            for j in self.y_list:
                self.block = Block(i, j)
                self.block_list.append(self.block)

        self.run()

    def run(self):
        self.playing = True

        while self.playing:
            self.events()
            self.update()

    def events(self):
        self.screen.onkey(self.paddle.move_right, 'Right')
        self.screen.onkey(self.paddle.move_left, 'Left')

    def update(self):

        self.screen.update()
        self.ball.move()

        # Block collision check
        for i in self.block_list:
            if i.ycor() - 20 <= self.ball.ycor() <= i.ycor() + 20 and (
                    i.xcor() - 60 < self.ball.xcor() < i.xcor() + 60) and self.ball.dy > 0:
                i.goto(1000, 1000)
                self.ball.dy *= -1
                self.block_list.remove(i)
        # Game over
        if len(self.block_list) < 0 or self.ball.ycor() < -270:
            self.playing = False
            self.ball.goto(1000, 1000)
            self.paddle.goto(1000, 1000)
            for i in self.block_list:
                i.goto(1000, 1000)

    def show_start_screen(self):
        self.waiting = True
        self.pen.goto(0, 0)
        self.screen.onkey(self.wait_for_keypress, 's')

        while self.waiting:
            self.screen.bgcolor('black')
            self.pen.write('Breakout Game \n\nAperte "s" para iniciar',
                           align='center', font=('8 Bit Wonder', 20, 'normal'))

    def show_game_over_screen(self):

        self.waiting = True
        self.pen.goto(0, 0)
        self.screen.onkey(self.wait_for_keypress, 's')

        while self.waiting:
            self.screen.bgcolor('black')
            self.pen.write(f'\tGame Over\n\nAperte "s" para um novo jogo.',
                           align='center', font=('8 Bit Wonder', 20, 'normal'))

    def wait_for_keypress(self):

        self.waiting = False


game = Game()
game.show_start_screen()

while True:
    game.new_game()
    game.show_game_over_screen()
