import config
import pygame
import math
import random


class Player:
    def __init__(self, colour, shot_colour, angle):
        # Sprites
        self.sprites = config.player_sprites
        self.scale = config.player_scale
        self.current_sprite = 0
        self.colour = colour
        self.shot_colour = shot_colour
        self.image = self.sprites[self.current_sprite].convert_alpha()
        self.colour_image = pygame.Surface(self.image.get_size()).convert_alpha()
        self.colour_image.fill(colour)
        self.width = config.player_scale[0]
        self.height = config.player_scale[1]
        self.coord = config.player_coord
        self.image.blit(self.colour_image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        # Coordinates
        self.initial_x = self.coord[0]
        self.initial_y = self.coord[1]
        self.angle = angle
        self.speed = config.player_speed
        self.radius = config.player_radius
        self.distance = self.radius
        self.x = self.initial_x + math.sin(math.radians(self.angle)) * self.radius
        self.y = self.initial_y + math.cos(math.radians(self.angle)) * self.radius

        # Rotated image
        self.rotation = pygame.sprite.Sprite()
        self.rotation = pygame.transform.scale(self.image, self.scale)
        self.rotation = pygame.transform.rotate(self.image, self.angle)
        self.rotation.blit(self.colour_image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.rect = self.rotation.get_rect()
        self.rect = self.image.get_rect(center=self.rect.center)

        # Hit box
        self.hit_box = self.rotation.get_rect()
        self.hit_box_colour = config.player_hit_box
        self.damage = False
        self.damage_cooldown = pygame.time.get_ticks()
        self.friendly_fire = 0

        # Score
        self.life = 3
        self.score = 0

    def move(self, direction):
        if direction == "right":
            self.angle += self.speed
        elif direction == "left":
            self.angle -= self.speed
        elif direction == "forward":
            self.radius -= self.speed * 2
        elif direction == "backward":
            self.radius += self.speed * 2

        # Space limiter
        self.radius = max(100, self.radius)
        self.radius = min(350, self.radius)

        self.x = self.initial_x + math.sin(math.radians(self.angle)) * self.radius
        self.y = self.initial_y + math.cos(math.radians(self.angle)) * self.radius

    # Sprites animation
    def animate(self):
        if self.current_sprite < len(self.sprites):
            self.image = self.sprites[self.current_sprite]
            self.rotation = pygame.transform.scale(self.image, self.scale)
            self.rotation = pygame.transform.rotate(self.rotation, self.angle)
            self.rotation.blit(self.colour_image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            self.current_sprite += 1
        else:
            self.current_sprite = 0

    def draw(self, screen, hit):
        if not hit:
            screen.blit(self.rotation, [self.x, self.y])

        # Update hit box
        self.hit_box.x = self.x + 5
        self.hit_box.y = self.y + 5
        self.hit_box.width = self.rotation.get_width() * 0.8
        self.hit_box.height = self.rotation.get_height() * 0.8

    # Shoot
    def fire(self):
        return Shot(self.x, self.y, self.width, self.height, self.angle, self.shot_colour)

    def change_colour(self, color):
        coloured_image = pygame.Surface(self.image.get_size())
        coloured_image.fill(color)

        final_image = self.image.copy()
        final_image.blit(coloured_image, (0, 0), special_flags=pygame.BLEND_MULT)
        return final_image


class Shot:
    def __init__(self, x, y, width, height, angle, colour):
        self.colour = colour
        # Coordinates
        self.radius = config.shot_radius
        self.pos = (x - self.radius/2, y - self.radius/2)
        self.x = x + width / 2 - (width / 2 * math.sin(math.radians(angle)))
        self.y = y + height / 2 - (height / 2 * math.cos(math.radians(angle)))
        self.angle = angle
        self.speed = config.shot_speed

        # Hit box
        self.hit_box = pygame.rect.Rect(self.x, self.y, self.radius, self.radius)
        self.hit_box_colour = config.shot_hit_box

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)

        # Update hit box
        self.hit_box.x = self.x
        self.hit_box.y = self.y

    def move(self):
        self.x -= math.sin(math.radians(self.angle)) * self.speed
        self.y -= math.cos(math.radians(self.angle)) * self.speed


class Button:
    def __init__(self, position):
        self.pos = position
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = config.button_width
        self.height = config.button_height
        self.colour = config.button_colour
        self.selected = config.button_selected
        self.image = pygame.rect.Rect(self.x - 25, self.y - 25, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.image)


class Asteroid:
    def __init__(self, asteroid):
        self.speed = random.randint(config.asteroid_min_speed, config.asteroid_max_speed)
        self.life = asteroid[0]
        self.size = asteroid[1]
        self.image = pygame.image.load(asteroid[2])
        self.image = pygame.transform.scale(self.image, self.size)
        self.rotation = pygame.transform.scale(self.image, self.size)
        self.x = config.center[0]
        self.y = config.center[1]
        self.angle = random.randint(-180, 180)
        self.rotation_angle = random.randint(-1, 1)
        self.hits = 0

        # Hit box
        self.hit_box = self.rotation.get_rect()
        self.hit_box_colour = config.asteroid_hit_box

    def move(self):
        self.x += math.cos(math.radians(self.angle))
        self.y += math.sin(math.radians(self.angle))
        self.rotation = pygame.transform.rotate(self.image, self.rotation_angle)
        self.rotation_angle += random.randint(1, 2)

    def draw(self, screen):
        screen.blit(self.rotation, [self.x, self.y])

        # Update hit box
        self.hit_box.width = self.rotation.get_width()
        self.hit_box.height = self.rotation.get_height()
        self.hit_box.x = self.x
        self.hit_box.y = self.y


class Alien:
    def __init__(self, alien, player):
        self.speed = random.randint(config.alien_min_speed, config.alien_max_speed)
        self.player = player
        self.life = alien[0]
        self.size = alien[1]
        self.image = pygame.image.load(alien[2])
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.center = config.center
        self.x = config.center[0]
        self.y = config.center[1]
        self.angle = random.randint(-180, 180)
        self.rotation_angle = random.randint(-1, 1)
        self.hits = 0
        self.start_time = pygame.time.get_ticks()  # tempo em que o alien foi criado

        # Hit box
        self.hit_box = self.image.get_rect()
        self.hit_box_colour = config.asteroid_hit_box

    def move(self):

        # calcula a direção para o jogador

        dx = self.player.x - self.rect.centerx
        dy = self.player.y - self.rect.centery
        angle = math.atan2(dy, dx)

        # move o alien em direção ao jogador
        if pygame.time.get_ticks() - self.start_time < 5000:  # ainda não passaram 5 segundos
            self.rect.centerx += self.speed * math.cos(angle)
            self.rect.centery += self.speed * math.sin(angle)
        else:  # já passaram 5 segundos
            self.rect.centerx += self.speed * math.cos(angle)
            self.rect.centery += self.speed * math.sin(angle)

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # desenha a imagem do alien na tela


        # Update hit box
        self.hit_box.x = self.rect.x
        self.hit_box.y = self.rect.y
        self.hit_box.width = self.image.get_width()
        self.hit_box.height = self.image.get_height() + 5


class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.images = []  # Lista de imagens para a animação
        self.current_frame = 0  # Índice da imagem atual
        self.frame_timer = 0  # Contador para o temporizador
        self.frame_delay = 50  # Intervalo de tempo para trocar de imagem
        self.load_images()

    def load_images(self):
        # Carrega a spritesheet da animação e adiciona cada imagem à lista de imagens
        # Substitua essa função com a lógica para carregar a spritesheet da sua animação
        for i in range(8):
            image = pygame.image.load(f"sprites/Efeito_de_explosao.png")
            self.images.append(image)

    def update(self):
        self.frame_timer += 1
        if self.frame_timer >= self.frame_delay:
            # Atualiza a imagem atual da animação
            self.current_frame += 1
            if self.current_frame >= len(self.images):
                # Se chegou no fim da animação, remove a instância da lista de explosões
                self.images.remove(self)
            else:
                # Reinicia o temporizador
                self.frame_timer = 0

    def draw(self, screen):
        # Desenha a imagem atual da animação na tela
        image = self.images[self.current_frame]
        rect = image.get_rect()
        rect.center = (self.x, self.y)
        screen.blit(image, rect)


class HUD:
    def __init__(self):
        self.font = config.hud_font
        self.colour = config.hud_font_colour
        self.lives_colour_1 = config.player_1_colour
        self.lives_colour_2 = config.player_2_colour
        self.size = config.hud_font_size
        self.hud = pygame.font.Font(self.font, self.size)
        self.score = 0

        self.score_pos = (25, 10)
        self.lives_1_pos = (config.screen_width - 40, 10)
        self.lives_2_pos = (config.screen_width - 40, 50)

    def write_score(self, screen):
        if self.score == config.bryan_adams:
            label = self.hud.render(f'{self.score}   NICE!', True, self.colour)
        elif self.score == config.leave_your_nets:
            label = self.hud.render(f'4:20   WOW!', True, self.colour)
        else:
            label = self.hud.render(f'{self.score}', True, self.colour)
        screen.blit(label, self.score_pos)

    def write_lives(self, screen, lives_1, lives_2):
        if lives_1 == 0:
            label_1 = self.hud.render('X', True, self.lives_colour_1)
        else:
            label_1 = self.hud.render(f'{lives_1}', True, self.lives_colour_1)
        if lives_2 == 0:
            label_2 = self.hud.render('X', True, self.lives_colour_2)
        else:
            label_2 = self.hud.render(f'{lives_2}', True, self.lives_colour_2)
        screen.blit(label_1, self.lives_1_pos)
        screen.blit(label_2, self.lives_2_pos)
