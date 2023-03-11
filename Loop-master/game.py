import math
import pygame
import classes
import config
from random import choice
from random import randint

pygame.init()
pygame.font.init()
pygame.joystick.init()

screen = pygame.display.set_mode(config.resolution)
icon = pygame.image.load(config.icon)
pygame.display.set_caption('Space Treko')
pygame.display.set_icon(icon)
center = config.center
logo = config.logo
background_image = config.background
text_list = config.text_list

# Sounds
sfx_play = config.sfx_play
sfx_shot = config.sfx_shot
sfx_hit = config.sfx_hit
sfx_hit_alien = config.sfx_hit_alien
sfx_hit_player = config.sfx_hit_player
sfx_game_over = config.sfx_game_over
bgm_start = config.bgm_start
bgm = config.bgm_game

# Creating players
player_1_colour = config.player_1_colour
player_1_shot_colour = config.player_1_shot
player_1_angle = config.player_1_angle
player_2_colour = config.player_2_colour
player_2_shot_colour = config.player_2_shot
player_2_angle = config.player_2_angle
player_1 = classes.Player(player_1_colour, player_1_shot_colour, player_1_angle)
player_2 = classes.Player(player_2_colour, player_2_shot_colour, player_2_angle)
players = [player_1, player_2]
blink = False

# Player events
animation = pygame.USEREVENT + 1
pygame.time.set_timer(animation, 50)

# Creating asteroids
asteroids_lvl1 = config.asteroids_list[:4]
asteroids_lvl2 = config.asteroids_list[:7]
asteroids_lvl3 = config.asteroids_list[:10]
asteroids = []

# Asteroids events
pop_asteroid = pygame.USEREVENT + 2
asteroid_spawn_max = config.asteroid_spawn_max
asteroid_spawn_min = config.asteroid_spawn_min
pygame.time.set_timer(pop_asteroid, randint(asteroid_spawn_min, asteroid_spawn_max))

# Creating aliens
aliens_list = config.aliens_list
aliens = []
pop_alien = pygame.USEREVENT + 3
alien_spawn_max = config.alien_spawn_max
alien_spawn_min = config.alien_spawn_min
pygame.time.set_timer(pop_alien, randint(alien_spawn_min, alien_spawn_max))

# Planet
planet = pygame.image.load(config.planet[1])
planet_rotation = pygame.transform.scale(planet, config.planet[0])
planet_position = (center[0] - config.planet[0][0] / 2, center[1] - config.planet[0][1] / 2)
planet_angle = 0
planet_scale = 0

shots = []
shot_rate = config.shot_rate
shot_cooldown_1 = False
shot_cooldown_2 = False
shot_rate_1 = pygame.time.get_ticks()
shot_rate_2 = pygame.time.get_ticks()
friendly_fire = True

level = 1
hud = classes.HUD()

clock = pygame.time.Clock()

run_game = True

# Players movement conditions
p1_forward = False
p1_backward = False
p1_move_left = False
p1_move_right = False
p2_forward = False
p2_backward = False
p2_move_left = False
p2_move_right = False


def start_screen(window, background_image_path, logo_image_path, music_path):
    # Carrega a imagem de fundo
    background_image = background_image_path
    # Obtém as dimensões da tela
    screen_width, screen_height = pygame.display.get_surface().get_size()
    # Redimensiona a imagem de fundo para preencher a tela
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    # Define a posição da imagem de fundo na tela
    background_position = (0, 0)

    # Carrega a imagem da logo
    logo_image = pygame.image.load(logo_image_path)
    # Redimensiona a imagem da logo
    logo_image = pygame.transform.scale(logo_image, (int(screen_width * 0.8), int(screen_height * 0.2)))
    # Define a posição da imagem da logo na tela
    logo_position = ((screen_width - logo_image.get_width()) // 2, screen_height * 0.2)

    # Carrega a música de abertura
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(1)
    pygame.mixer.music.fadeout(10000)

    window.blit(background_image, background_position)
    pygame.display.flip()

    pygame.time.delay(3000)

    # Loop principal da tela de start
    while True:
        # Processa eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Encerra o jogo se o usuário clicar no botão de fechar
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                pygame.mixer.music.stop()
                return

        # Desenha a imagem de fundo na tela
        window.blit(background_image, background_position)

        # Desenha a imagem da logo na tela
        window.blit(logo_image, logo_position)

        # Atualiza a tela
        pygame.display.flip()


def game_over_screen(screen, text_list, music_path):
    global background_image

    continue_game = False
    # Escolhe um texto aleatório da lista
    game_over_text = choice(text_list)
    # Define a fonte e tamanho do texto
    font = pygame.font.Font(config.hud_font, 55)
    # Obtém as dimensões do texto renderizado
    text_1 = font.render(game_over_text[0], True, (255, 255, 255))
    text_1_width, text_1_height = font.size(game_over_text[0])
    text_2 = font.render(game_over_text[1], True, (255, 255, 255))
    text_2_width, text_2_height = font.size(game_over_text[1])
    # Obtém o tamanho da tela
    screen_width, screen_height = pygame.display.get_surface().get_size()
    # Define a posição do texto na tela
    x1 = (screen_width - text_1_width) / 2
    y1 = (screen_height - text_1_height) / 2 - 35
    x2 = (screen_width - text_2_width) / 2
    y2 = (screen_height - text_2_height) / 2 + 35

    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(1)

    while not continue_game:
        screen.blit(background_image, (0, 0))
        # Desenha o texto na tela
        screen.blit(text_1, (x1, y1))
        screen.blit(text_2, (x2, y2))
        # Atualiza a tela
        if event.type == pygame.KEYDOWN:
            pygame.mixer.music.stop()
            return

        pygame.display.flip()


start_screen(screen, background_image, logo, bgm_start)

pygame.mixer.music.load(sfx_game_over)
pygame.mixer.music.load(sfx_hit_player)
pygame.mixer.music.load(sfx_hit_alien)
pygame.mixer.music.load(sfx_hit)
pygame.mixer.music.load(sfx_shot)
pygame.mixer.music.load(sfx_play)
pygame.mixer.Channel(0).play(pygame.mixer.Sound(sfx_play))

pygame.mixer.music.load(bgm)
pygame.mixer.music.play(-1)

pygame.time.delay(2000)

while run_game:
    time = pygame.time.get_ticks()
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        # Quitting conditions
        if event.type == pygame.QUIT:
            run_game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run_game = False

        # Commands
        if event.type == pygame.KEYDOWN:
            if player_1.life > 0:
                if event.key in config.p1_forward:
                    p1_forward = True
                if event.key in config.p1_backward:
                    p1_backward = True
                if event.key in config.p1_left:
                    p1_move_left = True
                if event.key in config.p1_right:
                    p1_move_right = True
                if event.key in config.p1_fire:
                    if not shot_cooldown_1:
                        shots.append(player_1.fire())
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound(sfx_shot))
                        shot_rate_1 = pygame.time.get_ticks()
            if player_2.life > 0:
                if event.key in config.p2_forward:
                    p2_forward = True
                if event.key in config.p2_backward:
                    p2_backward = True
                if event.key in config.p2_left:
                    p2_move_left = True
                if event.key in config.p2_right:
                    p2_move_right = True
                if event.key in config.p2_fire:
                    if not shot_cooldown_2:
                        shots.append(player_2.fire())
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(sfx_shot))
                        shot_rate_2 = pygame.time.get_ticks()
        if event.type == pygame.KEYUP:
            if event.key in config.p1_forward:
                p1_forward = False
            if event.key in config.p1_backward:
                p1_backward = False
            if event.key in config.p1_left:
                p1_move_left = False
            if event.key in config.p1_right:
                p1_move_right = False
            if event.key in config.p2_forward:
                p2_forward = False
            if event.key in config.p2_backward:
                p2_backward = False
            if event.key in config.p2_left:
                p2_move_left = False
            if event.key in config.p2_right:
                p2_move_right = False

        # Spawning asteroids
        if event.type == pop_asteroid:
            if level == 1:
                asteroids.append(classes.Asteroid(choice(asteroids_lvl1)))
            if level == 2:
                asteroids.append(classes.Asteroid(choice(asteroids_lvl2)))
            if level == 3:
                asteroids.append(classes.Asteroid(choice(asteroids_lvl3)))
            pygame.time.set_timer(pop_asteroid, randint(asteroid_spawn_min, asteroid_spawn_max))

        # Spawning aliens
        if event.type == pop_alien:
            if len(players) > 0:
                aliens.append(classes.Alien(choice(aliens_list), choice(players)))
            pygame.time.set_timer(pop_alien, randint(alien_spawn_min, alien_spawn_max))

        # Sprites animation
        if event.type == animation:
            player_1.animate()
            player_2.animate()

    # Player 1 movement*
    if p1_forward:
        player_1.move('forward')
    if p1_backward:
        player_1.move('backward')
    if p1_move_left:
        player_1.move('left')
    if p1_move_right:
        player_1.move('right')

    # Player 2 movement
    if p2_forward:
        player_2.move('forward')
    if p2_backward:
        player_2.move('backward')
    if p2_move_left:
        player_2.move('left')
    if p2_move_right:
        player_2.move('right')

    if pygame.time.get_ticks() - shot_rate_1 < shot_rate:
        shot_cooldown_1 = True
        friendly_fire = False
    else:
        shot_cooldown_1 = False
        friendly_fire = True
    if pygame.time.get_ticks() - shot_rate_2 < shot_rate:
        shot_cooldown_2 = True
        friendly_fire = False
    else:
        shot_cooldown_2 = False
        friendly_fire = True

    # Drawing players
    for player in players:
        if pygame.time.get_ticks() - player.damage_cooldown < 2000:
            if pygame.time.get_ticks() % 2 == 0:
                blink = not blink
            player.draw(screen, blink)
        else:
            blink = False
            player.damage = False
            player.draw(screen, False)
        if player.life == 0:
            players.remove(player)

    # Player-player collision
    if player_1.hit_box.colliderect(player_2.hit_box):
        if time > 1000:
            if not player_1.damage and not player_2.damage:
                player_1.damage = True
                player_2.damage = True
                player_1.life -= 1
                player_2.life -= 1
                player_1.damage_cooldown = pygame.time.get_ticks()
                player_2.damage_cooldown = pygame.time.get_ticks()

    # Drawing bullets
    for bullet in shots:
        bullet.draw(screen)
        bullet.move()
        if math.dist((bullet.x, bullet.y), bullet.pos) > math.dist(bullet.pos, center):
            shots.remove(bullet)

        # Friendly fire
        for player in players:
            if player.hit_box.colliderect(bullet.hit_box):
                if friendly_fire:
                    pygame.draw.circle(screen, config.explosion_colour, (bullet.x, bullet.y), bullet.radius * 5)
                    shots.remove(bullet)
                    player.friendly_fire += 1
                    if player.friendly_fire == 3:
                        hud.score -= 1
                        player.life -= 1
                        player.friendly_fire = 0

    # Drawing asteroids
    for rock in asteroids:
        rock.draw(screen)
        rock.move()

        # Asteroid-player collision
        for player in players:
            if rock.hit_box.colliderect(player.hit_box):
                if not player.damage:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound(sfx_hit_player))

                    player.life -= 1
                    player.damage_cooldown = pygame.time.get_ticks()
                    player.damage = True
                    pygame.draw.circle(screen, config.damage_colour, (player.x, player.y), 25)
                    asteroids.remove(rock)

        # Asteroid-bullet collision
        for bullet in shots:
            if rock.hit_box.colliderect(bullet.hit_box):
                pygame.mixer.Channel(3).play(pygame.mixer.Sound(sfx_hit))

                pygame.draw.circle(screen, config.explosion_colour, (bullet.x, bullet.y), bullet.radius * 5)
                shots.remove(bullet)
                rock.hits += 1
                if rock.hits == rock.life:
                    hud.score += rock.life * 3
                    asteroids.remove(rock)

        # Asteroids de-spawning
        if rock.x > config.screen_width or rock.x < 0:
            asteroids.remove(rock)
        elif rock.y > config.screen_height or rock.y < 0:
            asteroids.remove(rock)

    # Drawing aliens
    for et in aliens:
        et.move()
        et.draw(screen)

        # Alien-bullet collision
        for bullet in shots:
            if et.hit_box.colliderect(bullet.hit_box):
                pygame.mixer.Channel(4).play(pygame.mixer.Sound(sfx_hit_alien))

                pygame.draw.circle(screen, config.explosion_colour, (bullet.x, bullet.y), bullet.radius * 5)
                shots.remove(bullet)
                et.hits += 1
                if et.hits == et.life:
                    hud.score += et.life * 3
                    pygame.draw.circle(screen, config.explosion_colour, (et.rect.centerx, et.rect.centery), 5)
                    aliens.remove(et)

        # Alien-asteroid collision
        for rock in asteroids:
            if et.hit_box.colliderect(rock.hit_box):
                pygame.mixer.Channel(4).play(pygame.mixer.Sound(sfx_hit_alien))

                pygame.draw.circle(screen, config.explosion_colour, (et.rect.centerx, et.rect.centery), 5)
                aliens.remove(et)
                asteroids.remove(rock)

        # Alien-player collision
        for player in players:
            if et.hit_box.colliderect(player.hit_box):
                if not player.damage:
                    pygame.mixer.Channel(5).play(pygame.mixer.Sound(sfx_hit_player))

                    player.life -= 1
                    player.damage_cooldown = pygame.time.get_ticks()
                    player.damage = True
                    pygame.draw.circle(screen, config.damage_colour, (player.x, player.y), 25)
                    aliens.remove(et)
                    if player.life == 0:
                        players.remove(player)

    # Difficulty progression
    if 30 < hud.score < 69:
        level = 2

    elif hud.score > 69:
        level = 3

    # Drawing central planet
    screen.blit(planet_rotation, planet_position)
    planet_angle -= 1
    planet_rotation = pygame.transform.rotate(planet, planet_angle)
    planet_rotation = pygame.transform.scale(planet_rotation, config.planet[0])

    hud.write_score(screen)
    hud.write_lives(screen, player_1.life, player_2.life)

    if player_1.life == 0 and player_2.life == 0:
        pygame.mixer.music.stop()
        game_over_screen(screen, text_list, sfx_game_over)

    clock.tick(60)
    pygame.display.flip()
