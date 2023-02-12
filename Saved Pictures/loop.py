import pygame
import constates
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

        diretorio_imagens = os.path.join(os.getcwd(), "imagens")
        self.diretorio_audio = os.path.join(os.getcwd(), "audio")
        self.spritesheet = os.path.join(diretorio_imagens, constates.SPRITESHEETS)
        logo_jogo_start = os.path.join(diretorio_imagens, constates.LOGOJOGO)
        self.logo_jogo_start = pygame.image.load(logo_jogo_start).convert()

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

        self.mostrar_start_logo(constates.x / 2, 20)
        self.mostrar_texto('Pressione qualquer tecla para jogar', 32, constates.BRANCO, constates.x/2, 320)

        pygame.display.flip()
        self.esperar_jogador()

        self.mostrar_texto('Desenvolvido por Machado Lins Productions®', 19, constates.BRANCO, constates.x / 2, 570)

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
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.diretorio_audio, )).play()

    def mostrar_tela_game_over(self):
        pass


g = Game()
g.mostrar_tela_start()

while g.rodando:
    g.novo_jogo()
    g.mostrar_tela_game_over()


