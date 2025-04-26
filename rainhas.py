

# Primeiro, definir como elas serao representadas 
# Gerar aleatoriamente a posicao inicial
# Calcular os ataques
# Iterativamente, de rainha em rainha, gera uma vizinhanca, 
# e assim que encontrar um valor menor de ataques, ela muda o estado
# se nao encontrar um valor menor de ataques, para o algoritmo (ou em ataques = 0)

import random
import pygame
import sys

# Essa funcao calcula quantos ataques existem no tabuleiro, como as rainhas estao sempre na mesma coluna,
# ele verifica se elas estao na mesma linha ou na mesma diagonal.
# teste
def CalcularAtaques(estado):
    ataques = 0
    for i in range(len(estado)):
        for j in range(i+1, len(estado)):
            if(estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j)):
                ataques = ataques + 1
    return ataques

def TestarVizinhos(estado): 
    ataques = CalcularAtaques(estado)
    estadoNovo = estado.copy()
    for i in range(len(estado)):
        for j in range(len(estado)):
            estadoNovo[i] = j
            if CalcularAtaques(estadoNovo) < ataques:
                print("Um novo melhor estado foi encontrado!\n")
                print (estadoNovo)
                return estadoNovo
            estadoNovo[i]=estado[i]
    print("Erro: esse já é o melhor local")
    print(estado)
    return estado

def CalcularMelhorEstado(estado): 
    estadoVizinho = TestarVizinhos(estado)
    print("original: " + str(CalcularAtaques(estado)))
    print("novo: "+ str(CalcularAtaques(estadoVizinho)))
    while(CalcularAtaques(estado) > CalcularAtaques(estadoVizinho)):
        print("original: " + str(CalcularAtaques(estado)))
        print("novo: "+ str(CalcularAtaques(estadoVizinho)))
        estado = estadoVizinho.copy()
        estadoVizinho = TestarVizinhos(estado)
    return estado



def desenhar_tabuleiro(estado):
    N = 8
    TILE_SIZE = 80
    SCREEN_SIZE = N * TILE_SIZE

    WHITE = (255, 255, 255)
    GRAY = (150, 150, 150)
    RED = (255, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption('8 Rainhas - Estado fornecido')

    font = pygame.font.SysFont("segoe-ui-symbol.ttf",64)

    running = True
    while running:
        screen.fill(WHITE)

        for row in range(N):
            for col in range(N):
                rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if (row + col) % 2 == 0:
                    pygame.draw.rect(screen, GRAY, rect)
                else:
                    pygame.draw.rect(screen, WHITE, rect)

        # Desenhar as rainhas
        for col, row in enumerate(estado):
            text = font.render(u'♛', True, RED)
            screen.blit(text, (col * TILE_SIZE + 20, row * TILE_SIZE + 20))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()




    

# O estado inicial é um vetor prenchido com os numeros de 1 a 8 de forma aleatoria. O índice do vetor
# determina a coluna da rainha, e o seu valor determina a linha em que a rainha se encontra. 
estado = list(range(0, 8))
random.shuffle(estado)
print("\n\n")
MelhorEstado = CalcularMelhorEstado(estado)
desenhar_tabuleiro(MelhorEstado)

