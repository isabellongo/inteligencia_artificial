

# Primeiro, definir como elas serao representadas 
# Gerar aleatoriamente a posicao inicial
# Calcular os ataques
# Iterativamente, de rainha em rainha, gera uma vizinhanca, 
# e assim que encontrar um valor menor de ataques, ela muda o estado
# se nao encontrar um valor menor de ataques, para o algoritmo (ou em ataques = 0)

import random
import pygame

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
    listaEstados = list()
    listaEstados.append(estado)
    listaEstados.append(estadoVizinho)
    print("original: " + str(CalcularAtaques(estado)))
    print("novo: "+ str(CalcularAtaques(estadoVizinho)))
    while(CalcularAtaques(estado) > CalcularAtaques(estadoVizinho)):
        print("original: " + str(CalcularAtaques(estado)))
        print("novo: "+ str(CalcularAtaques(estadoVizinho)))
        estado = estadoVizinho.copy()
        estadoVizinho = TestarVizinhos(estado)
        if(estado != estadoVizinho):
            listaEstados.append(estadoVizinho)
    return listaEstados




def animar_tabuleiro(estados, listaAtaques):
    N = 8
    TILE_SIZE = 80
    BOARD_SIZE = N * TILE_SIZE
    SCREEN_HEIGHT = BOARD_SIZE + 40  # board + counter

    WHITE = (255, 255, 255)
    GRAY = (150, 150, 150)
    BLACK = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode((BOARD_SIZE, SCREEN_HEIGHT))
    pygame.display.set_caption('Problema das 8 rainhas - Hill Climbing')

    font = pygame.font.SysFont("Segoe UI Symbol", 64)
    counter_font = pygame.font.SysFont("Arial", 24)

    frame = 0
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(WHITE)

        # Draw chessboard 
        for row in range(N):
            for col in range(N):
                rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if (row + col) % 2 == 0:
                    pygame.draw.rect(screen, GRAY, rect)
                else:
                    pygame.draw.rect(screen, WHITE, rect)

        # Draw queens 
        estado = estados[frame]
        for col, row in enumerate(estado):
            text = font.render(u'♛', True, BLACK)
            text_rect = text.get_rect(center=(
                col * TILE_SIZE + TILE_SIZE // 2,
                row * TILE_SIZE + TILE_SIZE // 2
            ))
            screen.blit(text, text_rect)

        # Draw counter below the board
        counter_text = counter_font.render(f"Estado {frame + 1} de {len(estados)}", True, BLACK)
        screen.blit(counter_text, (10, BOARD_SIZE + 5))  # y = bottom of board + margin
        attack_text = counter_font.render(f"Ataques: {listaAtaques[frame]}", True, BLACK)
        screen.blit(attack_text, (500, BOARD_SIZE + 5))

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move to next frame after delay
        pygame.time.delay(1500)
        if frame < len(estados) - 1:
            frame += 1
        else:
            # Stop at last frame
            pass

        clock.tick(60)

    pygame.quit()




    

# O estado inicial é um vetor prenchido com os numeros de 1 a 8 de forma aleatoria. O índice do vetor
# determina a coluna da rainha, e o seu valor determina a linha em que a rainha se encontra. 
estado = list(range(0, 8))
random.shuffle(estado)
listaEstados = CalcularMelhorEstado(estado)
listaAtaques = list()
for x in listaEstados:
    listaAtaques.append(CalcularAtaques(x))

print("\n\n")

animar_tabuleiro(listaEstados, listaAtaques)

