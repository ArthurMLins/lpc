import pygame
import math
from draw_screen import draw_object

pygame.init()
pygame.font.init()

# color balls
green = (0, 255, 0)
blue = (0, 0, 255)

# score´s
score1 = 0
score2 = 0

# Screen
sc_width = 1000
sc_height = 750
screen = pygame.display.set_mode((sc_width, sc_height))
border = 25
screen.fill("#9f4100")
pygame.display.set_caption("Breakout Game")
font = pygame.font.Font("PressStart2P.ttf", 40)

# Score (player 1)
score_point_player1 = font.render("0", True, (0, 255, 0))
score_point_player1_rect = score_point_player1.get_rect()
score_point_player1_rect.center = (sc_width / 4, 25)
# Score (player 2)
score_point_player2 = font.render("0", True, (0, 0, 255))
score_point_player2_rect = score_point_player2.get_rect()
score_point_player2_rect.center = (3 * sc_width / 4, 25)

# ball from left tank
ball_x_left = -5
ball_y_left = -5
ball_dx_left = 0
ball_dy_left = 0
ball_left = pygame.draw.rect(screen, green, (ball_x_left, ball_y_left, 5, 5))
count_balls_left = 3

# ball from right tank
ball_x_right = -5
ball_y_right = -5
ball_dx_right = 0
ball_dy_right = 0
ball_right = pygame.draw.rect(screen, green, (ball_x_right, ball_y_right, 5, 5))
count_balls_right = 4
# Load images
player1 = pygame.sprite.Sprite()
player2 = pygame.sprite.Sprite()


def load_images(sprite, ang, xp, yp, image):
    sprite.image = pygame.image.load(image)
    sprite.image = pygame.transform.scale(sprite.image, (50, 50))
    sprite.image = pygame.transform.rotate(sprite.image, ang)
    cor_x = sprite.image.get_rect(center=(xp + 25, yp + 25))
    sprite.rect = cor_x
    return cor_x


xp1 = 50
yp1 = 380
xp2 = sc_width - 100
yp2 = 380
radius = 25 * (2 ** 0.5)

ang_left = 0
ang_left_death = 0
left_death_count = 0

ang_right = 0
ang_right_death = 0
right_death_count = 0
count = 0
clock = pygame.time.Clock()
per_1 = False
per_2 = False
game_loop = True
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    blue = (0, 0, 255)

    player1_cor = load_images(player1, ang_left, xp1, yp1, "player1.png")
    player2_cor = load_images(player2, ang_right, xp2, yp2, "player2.png")
    player2.image = pygame.transform.rotate(player2.image, 180)

    # collision player 1 with objects
    collision_1 = (
        25 + xp1 + 25 * math.cos(math.radians(ang_left)), yp1 + 25 * math.sin(math.radians(ang_left)), 5,
        50)
    if draw_object(screen, collision_1):
        per_1 = True
    else:
        per_1 = False

    # collision player 2 with objects
    collision_2 = (
        25 + xp2 - 25 * math.sin(math.radians(ang_right + 90)), yp2 - 25 * math.cos(math.radians(ang_right + 90)), 5,
        50)
    if draw_object(screen, collision_2):
        per_2 = True
    else:
        per_2 = False

    # Move p1
    if keys[pygame.K_w] and per_1:
        xp1 += math.cos(math.radians(ang_left))
        yp1 -= math.sin(math.radians(ang_left))

    elif keys[pygame.K_a]:
        ang_left += 1

    elif keys[pygame.K_d]:
        ang_left += -1

    # start player 1 ball
    elif keys[pygame.K_q] and count_balls_left >= 3:
        ball_x_left = 25 + xp1 + 25 * math.cos(math.radians(ang_left))
        ball_y_left = 25 + yp1 - 25 * math.sin(math.radians(ang_left))
        ball_left = pygame.draw.rect(screen, green, (ball_x_left, ball_y_left, 5, 5))
        ball_dx_left = math.cos(math.radians(ang_left))
        ball_dy_left = -math.sin(math.radians(ang_left))
        count_balls_left = 0

    # Move p2
    if keys[pygame.K_UP] and per_2:
        xp2 += math.cos(math.radians(ang_right + 180))
        yp2 -= math.sin(math.radians(ang_right + 180))

    elif keys[pygame.K_LEFT]:
        ang_right += 1

    elif keys[pygame.K_RIGHT]:
        ang_right += -1

    # start player 2 ball
    elif keys[pygame.K_SEMICOLON] and count_balls_right >= 3:
        ball_x_right = 25 + xp2 + 25 * math.cos(math.radians(ang_right + 180))
        ball_y_right = 25 + yp2 - 25 * math.sin(math.radians(ang_right + 180))
        ball_right = pygame.draw.rect(screen, blue, (ball_x_right, ball_y_right, 5, 5))
        ball_dx_right = math.cos(math.radians(ang_right + 180))
        ball_dy_right = -math.sin(math.radians(ang_right + 180))
        count_balls_right = 0

    # check ball collisions with objects

    if not draw_object(screen, ball_left):
        ball_dy_left *= -1
        ball_x_left = ball_x_left + ball_dx_left
        ball_y_left = ball_y_left + ball_dy_left
        ball_left = pygame.draw.rect(screen, green, (ball_x_left, ball_y_left, 5, 5))
        if not draw_object(screen, ball_left):
            ball_dx_left *= -1
            count_balls_left -= 1
        count_balls_left += 1

    # check ball collision with player 2
    if ball_left.colliderect(player2):
        score1 += 1
        score_point_player1 = font.render(str(score1), True, (0, 255, 0))
        count_balls_left += 3
        ang_right_death = 10
        right_death_count = 0

    if right_death_count <= 144:
        if right_death_count == 144:
            xp2 = sc_width - 100

            if score1 % 2 == 0 and score1 != 0:
                yp2 = 100
                ang_right = 0
            elif score1 % 2 == 1 and score1 != 0:
                yp2 = 650
                ang_right = 0

        right_death_count += 1
        ang_right += ang_right_death

    # check ball collisions with objects
    if not draw_object(screen, ball_right):
        ball_dy_right *= -1
        ball_x_right = ball_x_right + ball_dx_right
        ball_y_right = ball_y_right + ball_dy_right
        ball_right = pygame.draw.rect(screen, blue, (ball_x_right, ball_y_right, 5, 5))
        if not draw_object(screen, ball_right):
            ball_dx_right *= -1
            count_balls_right -= 1
        count_balls_right += 1

    # check ball collision with player 1
    if ball_right.colliderect(player1):
        score2 += 1
        score_point_player2 = font.render(str(score2), True, (0, 0, 255))
        count_balls_right += 3
        ang_left_death = 10
        left_death_count = 0

    if left_death_count <= 144:
        left_death_count += 1
        ang_left += ang_left_death

        if left_death_count == 144:
            xp1 = 50
            if score2 % 2 == 0 and score2 != 0:
                yp1 = 100
                ang_left = 0
            elif score2 % 2 == 1 and score2 != 0:
                yp1 = 650
                ang_left = 0

    if count_balls_right >= 3:
        ball_x_right = - 100
        ball_y_right = - 100

    if count_balls_left >= 3:
        ball_x_left = -100
        ball_y_left = -100

    ball_x_left = ball_x_left + ball_dx_left
    ball_y_left = ball_y_left + ball_dy_left

    ball_x_right = ball_x_right + ball_dx_right
    ball_y_right = ball_y_right + ball_dy_right

    screen.blit(player1.image, player1_cor)
    screen.blit(player2.image, player2_cor)

    screen.blit(score_point_player1, score_point_player1_rect)
    screen.blit(score_point_player2, score_point_player2_rect)

    ball_left = pygame.draw.rect(screen, green, (ball_x_left, ball_y_left, 5, 5))
    ball_right = pygame.draw.rect(screen, blue, (ball_x_right, ball_y_right, 5, 5))

    draw_object(screen, player1.rect)

    pygame.display.flip()
    screen.fill("#9f4100")
    clock.tick(130)
