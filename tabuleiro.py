import pygame
import sys


# Inicializando o pygame
pygame.init()
tela = pygame.display.set_mode((640, 640))
pygame.display.set_caption('Jogo de Xadrez v0.0')

# Carregando a imagem do tabuleiro
tabuleiro_img = pygame.image.load('./imagens/tabuleiro/chess_board.jpg')

# Redimensionando a imagem do tabuleiro para o tamanho da tela
tabuleiro_img = pygame.transform.scale(tabuleiro_img, (640, 640))

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Desenhando a imagem do tabuleiro na tela
    tela.blit(tabuleiro_img, (0, 0))

    # Atualizando a tela (Vai ser usado futuramente quando for add peças e elas mudaremde posições)
    pygame.display.flip()
