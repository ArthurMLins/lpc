import pygame
import constates
import os
import math


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constates.LAR, constates.ALT))
        pygame.display.set_caption(constates.Title)
        self.timer = pygame.time.Clock()
        self.rodando = True
        self.font = pygame.font.match_font('Grand9K Pixel.ttf')
        self.carregar_arquivos()

    def novo_jogo(self):
        # instancia as classes dos sprites do jogo
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):

        self.jogando = True
        while self.jogando:
            self.timer.tick(constates.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.rodando = False

    def atualizar_sprites(self):
        self.todas_as_sprites.update()

    def desenhar_sprites(self):

        self.tela.fill(constates.PRETO)
        self.todas_as_sprites.draw(self.tela)
        pygame.display.flip()

    def carregar_arquivos(self):

        diretorio_imagens = os.path.join(os.getcwd(), "imagens")
        self.diretorio_audio = os.path.join(os.getcwd(), "audio")
        self.spritesheet = os.path.join(diretorio_imagens, constates.SPRITESHEETS)
        logo_jogo_start = os.path.join(diretorio_imagens, constates.LOGOJOGO)
        self.logo_jogo_start = pygame.image.load(logo_jogo_start)

    def mostrar_texto(self, texto, tamanho, cor, x, y):

        fonte = pygame.font.Font(self.font, tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        self.tela.blit(texto, texto_rect)

    def mostrar_start_logo(self, x, y):
        start_logo_rect = self.logo_jogo_start.get_rect()
        start_logo_rect.midtop = (x, y)
        self.tela.blit(self.logo_jogo_start, start_logo_rect)

    def mostrar_tela_start(self):

        pygame.mixer.music.load(os.path.join(self.diretorio_audio, constates.ABERTURA))
        pygame.mixer.music.play()

        self.mostrar_start_logo(constates.LAR / 2, 100)
        self.mostrar_texto('Pressione qualquer tecla para jogar', 30, constates.BRANCO, constates.LAR - 500, 500)
        pygame.display.flip()
        self.esperar_jogador()
        self.mostrar_texto('Desenvolvido por Machado Lins Productions®', 19, constates.BRANCO, constates.LAR - 500, 300)

    def esperar_jogador(self):
        esperando = True
        while esperando:
            self.timer.tick(constates.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.rodando = False
                if event.type == pygame.KEYUP:
                    esperando = False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.diretorio_audio, )).play()
                if event.type == pygame.KEYUP:
                    esperando = False
                    self.novo_jogo()

    def mostrar_tela_game_over(self):
        pass


class Player:
    def __init__(self, x, y, radius, angle, distance):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = angle
        self.speed = 5
        self.distance = distance

    def update(self, direction):
        if direction == "right":
            self.angle += self.speed
        elif direction == "left":
            self.angle -= self.speed
        elif direction == "forward":
            self.distance += self.speed
        elif direction == "backward":
            self.distance -= self.speed

        self.distance = max(-180, self.distance)

        self.x = x + math.cos(math.radians(self.angle)) * (self.radius + self.distance)
        self.y = y + math.sin(math.radians(self.angle)) * (self.radius + self.distance)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 20)


x, y = 250, 250
radius = 200
player = Player(x, y, radius, 0, 0)

g = Game()
g.mostrar_tela_start()

while g.rodando:

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.update("right")
    elif keys[pygame.K_LEFT]:
        player.update("left")
    elif keys[pygame.K_UP]:
        player.update("forward")
    elif keys[pygame.K_DOWN]:
        player.update("backward")

    g.novo_jogo()
    g.mostrar_tela_game_over()
