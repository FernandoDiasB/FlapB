import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_FUNDO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bd.jpg')))
IMAGEM_DO_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png'))),
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 45)

class Passaro:
    IMGS = IMAGEM_DO_PASSARO

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = IMGS[0]

    def pular(self):
        self.velocidade = -10,5
        self.tempo = 0
        self.altura = self.y


    def mover_passaro(self):
        # calculo de deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        # restrição do movimento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2 #facilita na hora de pular

        self.y += deslocamento


        # ângulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50): # testar sem isso depois
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self,angulo -= self.VELOCIDADE_ROTACAO

    
    def desenhar(self, tela):
        # definir imagem que será usada
        self.contagem_imagem += 1
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem <self.TEMPO_ANIMACAO*4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem <self.TEMPO_ANIMACAO*4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        # quando o pássaro tá caindo
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            #tem um ajuste aqui

        # desenhar a imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        posicao_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center= posicao_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    #função que avalia a colisão de objetos
    def get_mask(self):
        pygame.mask.from_surface(self.imagem) 


       
class Cano:
    DISTANCIA = 200
    VELOCIDADE = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.posicao_topo = 0
        self.posicao_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO    
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 500)
        self.posicao_topo = self.altura - self.CANO_TOPO.get_height()
        self.posicao_base = self.altura + self.DISTANCIA

    def mover_cano(self):
        self.x -= self.VELOCIDADE

    def desenhar_cano(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.posicao_topo))
        tela.blit(self.CANO_BASE, (self.x, self.posicao_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.imagem)
        ...




class Chao:
    ...