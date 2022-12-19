import turtle

# Draw screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Creating the paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=0.8, stretch_len=5.0)
paddle.penup()
paddle.goto(0, -280)

# Draw ball
ball = turtle.Turtle()
ball.speed(0.7)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# Score
score = 0

# Head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(-280, 250)
hud.write("Score: 0", align="center", font=(" ", 32, "bold"))


def paddle_right():
    if paddle.xcor() < 350:
        paddle.setx(paddle.xcor() + 80)


def paddle_left():
    if paddle.xcor() > -350:
        paddle.setx(paddle.xcor() - 80)


def border_check():
    if ball.ycor() > 280:
        ball.dy *= -1
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.dx *= -1


def paddle_check():
    if -250 >= ball.ycor() >= -260 and ball.dy < 0:
        if ball.xcor() - 10 <= paddle.xcor() + 50 and ball.xcor() + 10 >= paddle.xcor() - 50:
            ball.dy *= -1


screen.listen()
screen.onkey(paddle_right, 'Right')
screen.onkey(paddle_left, 'Left')

block_list = []
colors = ['yellow', 'yellow', 'green', 'green', 'orange', 'orange', 'red', 'red']
position1 = []
position2 = []
# Blocks first position
y = 230

for i in range(8):
    y = y - 20
    x = -270
    for j in range(12):
        block = turtle.Turtle()
        block.speed()
        block.color(colors[i])
        block.shape('square')
        block.shapesize(stretch_wid=0.5, stretch_len=2.0)
        block.penup()
        block.goto(x, y)
        block_list.append(block)
        position1.append(x)
        position2.append(y)

        x = x + 49

block_count = len(block_list)
while block_count > 0:

    screen.update()
    ball.goto(ball.xcor() + ball.dx, ball.ycor() + ball.dy)
    border_check()
    paddle_check()

    if ball.ycor() < -280:
        ball.goto(0, 0)
        ball.dx *= -1
        if score > 0:
            score -= 1
        hud.clear()
        hud.write(f"Score: {score}", align='center', font=(" ", 32, 'bold'))

    # Block collisions:
    for i in block_list:
        if ball.xcor() + 10 >= i.xcor() - 60 and ball.xcor() - 10 <= i.xcor() + 60:
            if i.ycor() - 20 <= ball.ycor() <= i.ycor() + 20:
                ball.dy *= -1
                i.goto(800, 800)
                score += 1
                block_count -= 1
                hud.clear()
                hud.write(f'Score: {score}', align='center', font=(" ", 32, 'bold'))


# Game Over
hud.clear()
hud.goto(0, 0)
hud.write(f'GAME OVER\nScore: {score}', align='center', font=('', 40, 'bold'))
