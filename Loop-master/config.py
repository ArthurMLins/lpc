import pygame
import os

# Display
resolution = (900, 900)
screen_width = resolution[0]
screen_height = resolution[1]
center = (screen_width / 2, screen_height / 2)
icon = 'sprites/loop_spritesheet6.png'
logo = 'sprites/loop_logo.png'

#
background = pygame.image.load('sprites/loop_background.png')
background = pygame.transform.scale(background, resolution)

# Player
player_sprites = [pygame.image.load('sprites/airship1-2.png'),
                  pygame.image.load('sprites/airship2-2.png'),
                  pygame.image.load('sprites/airship3-2.png')]
p = 1/8
player_scale = (264*p, 447*p)
player_radius = 150
player_coord = [center[0], center[1]]
player_1_angle = 45
player_2_angle = -45
player_speed = 2
player_hit_box = (255, 0, 0)
player_1_colour = (100, 149, 237)
player_2_colour = 'darkorange1'
damage_colour = 'orange'

# Controls
p1_forward = [pygame.K_w]
p1_backward = [pygame.K_s]
p1_right = [pygame.K_d]
p1_left = [pygame.K_a]
p1_fire = [pygame.K_SPACE]

p2_forward = [pygame.K_UP]
p2_backward = [pygame.K_DOWN]
p2_right = [pygame.K_RIGHT]
p2_left = [pygame.K_LEFT]
p2_fire = [pygame.K_KP0]

# Shot
shot_radius = 2
shot_colour = 'white'
explosion_colour = 'orange'
shot_speed = 5
shot_rate = 300
player_1_shot = 'cyan3'
player_2_shot = 'orangered3'
shot_hit_box = (0, 0, 255)

# Asteroids
asteroid_spawn_min = 800
asteroid_spawn_max = 1200
asteroid_max_speed = 10
asteroid_min_speed = 5
a = 1/2
life_1 = 3
life_2 = 6
life_3 = 9
a1_1 = (life_1, (40*a, 33*a), os.path.join('sprites', 'asteroid_s1.png'))
a1_2 = (life_1, (46*a, 39*a), os.path.join('sprites', 'asteroid_s2.png'))
a1_3 = (life_1, (44*a, 46*a), os.path.join('sprites', 'asteroid_s3.png'))
a1_4 = (life_1, (31*a, 30*a), os.path.join('sprites', 'asteroid_s4.png'))
a1_5 = (life_1, (30*a, 39*a), os.path.join('sprites', 'asteroid_s5.png'))
a2_1 = (life_2, (84*a, 80*a), os.path.join('sprites', 'asteroid_m1.png'))
a2_2 = (life_2, (80*a, 64*a), os.path.join('sprites', 'asteroid_m2.png'))
a2_3 = (life_2, (62*a, 53*a), os.path.join('sprites', 'asteroid_m3.png'))
a3_1 = (life_3, (148*a, 103*a), os.path.join('sprites', 'asteroid_l1.png'))
a3_2 = (life_3, (117*a, 121*a), os.path.join('sprites', 'asteroid_l2.png'))
a3_3 = (life_3, (128*a, 120*a), os.path.join('sprites', 'asteroid_l3.png'))
asteroids_list = [a1_1, a1_2, a1_3, a1_4, a1_5, a2_1, a2_2, a2_3, a3_1, a3_2, a3_3]
asteroid_hit_box = (0, 255, 0)
ps = 1/4
planet = ((506*ps, 525*ps), os.path.join('sprites', 'asteroid_l2.png'))

# Aliens
alien_spawn_max = 8000
alien_spawn_min = 4000
alien_max_speed = 3
alien_min_speed = 2
life_4 = 6
life_5 = 7
alien_1 = (life_4, (102*a, 74*a), os.path.join('sprites', 'alien1.png'))
alien_2 = (life_5, (86*a, 49*a), os.path.join('sprites', 'alien2.png'))
aliens_list = [alien_1, alien_2]
alien_hit_box = (0, 255, 0)

# Buttons
button_width = 25
button_height = 25
button_colour = 'white'
button_selected = 'blue'
button_font = "Grand9K Pixel.ttf"

# Hud
hud_font = "Grand9K Pixel.ttf"
hud_font_colour = 'white'
hud_font_size = 40

# Tela game over

text_list = [["Asteroides de mais...", "ou habilidade de menos?"],
             ["Sorte sua que dá para", "reiniciar o jogo"],
             ["mano vcs sao mto burro.", "tipo assim"],
             ["O acidente não foi sua culpa,", "você precisa seguir em frente."],
             ["Keep calm,", "faz um jogo"]]

# Sounds
sfx_play = 'start.wav' #ação
sfx_shot = 'laser_gun.wav' #ação
sfx_hit = 'hit.wav' #colisão
sfx_hit_alien = 'mata alien.wav' #colisão
sfx_hit_player = 'taken hit player.wav' #colisão
sfx_game_over = 'gameover.wav'
bgm_start = 'Abertura_gamme_0001_master.wav'
bgm_game = 'Trilha_Game_0001.wav'

bryan_adams = 23 * 3
leave_your_nets = 60 * 7

# Listas das animações

shot_explosão = []
explosao = []
