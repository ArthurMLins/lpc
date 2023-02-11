import pygame
import constates
import sprites
import os


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constates.x, constates.y))
        pygame.display.set_caption(constates.Title)
        self.timer = pygame.time.Clock()
        self.rodando = True
        self.font = pygame.font.match_font(constates.FONTE)
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
                self.esta_rodando = False

    def atualizar_sprites(self):
        self.todas_as_sprites.update()

    def desenhar_sprites(self):

        self.tela.fill(constates.PRETO)
        self.todas_as_sprites.draw(self.tela)
        pygame.display.flip()

    def carregar_arquivos(self):

        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        self.diretorio_audio = os.path.join(os.getcwd(), 'audio')
        self.spritesheet = os.path.join(diretorio_imagens, 'constates.py.SPRITESHEET')
        self.logo_jogo_start = os.path.join(diretorio_imagens, constates.LOGOJOGO)
        self.logo_jogo_start = pygame.image.load(self.logo_jogo_start).convert()

    def mostrar_texto(self, texto, tamanho, cor, x, y):

        fonte = pygame.font.Font
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        texto.tela.blit(texto, texto_rect)

    def mostrar_start_logo(self):
        start_logo_rect = self.

    def mostrar_tela_start(self):
        self.mostrar_texto('Pressione uma tecla para jogar', 32, constates.BRANCO, constates.x/2, 320)

        pygame.display.flip()
        self.esperar_jogador()

        self.mostrar_texto('Desenvolvido por Machado Lins productions®', 19, constates.BRANCO, constates.x / 2, 570)

    def esperar_jogador(self):
        esperando = True
        while esperando:
            self.timer.tick(constates.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.esta_rodando = False
                if event.type == pygame.KEYUP:
                    esperando = False
    def mostrar_tela_game_over(self):
        pass


g = Game()
g.mostrar_tela_start()

while g.rodando:
    g.novo_jogo()
    g.mostrar_tela_game_over()
