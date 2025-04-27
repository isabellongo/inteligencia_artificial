import random
import pygame

# Essa função calcula quantos ataques existem no tabuleiro, como as rainhas estão sempre na mesma coluna,
# ele verifica se elas estao na mesma linha ou na mesma diagonal.

def CalcularAtaques(estado):
    ataques = 0
    for i in range(len(estado)):
        for j in range(i+1, len(estado)):
            if(estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j)):
                ataques = ataques + 1
    return ataques

# Verifica, uma coluna por vez, se há uma posição melhor para cada rainha, para na primeira posição que resulte em menos
# ataques, ou passa para a próxima coluna caso nenhuma seja encontrada, uma vez que todas as colunas sejam visitadas, retorna 
# o novo estado. 

def TestarVizinhos(estado): 
    ataques = CalcularAtaques(estado)
    estadoNovo = estado.copy()
    for i in range(len(estado)):
        for j in range(len(estado)):
            estadoNovo[i] = j
            if CalcularAtaques(estadoNovo) < ataques:
                return estadoNovo
            estadoNovo[i]=estado[i]
    return estado

# Itera a função TestarVizinhos até que não seja possível encontrar um estado vizinho com um número menor de ataques,
# adiciona o estado recebido em cada iteração a uma lista, de ordem decrescente de número de ataques 

def CalcularMelhorEstado(estado): 
    estadoVizinho = TestarVizinhos(estado)
    listaEstados = list()
    listaEstados.append(estado)
    listaEstados.append(estadoVizinho)
    while(CalcularAtaques(estado) > CalcularAtaques(estadoVizinho)):
        estado = estadoVizinho.copy()
        estadoVizinho = TestarVizinhos(estado)
        if(estado != estadoVizinho):
            listaEstados.append(estadoVizinho)
    return listaEstados

# Recebe a lista devolvida pela função CalcularMelhorEstado e faz uma animação representando a posição das rainhas em 
# cada estado, assim como o número da iteração e o número de ataques

def AnimarTabuleiro(estados, listaAtaques):
    N = 8
    TAMANHO_QUADRADO = 80
    TAMANHO_TABULEIRO = N * TAMANHO_QUADRADO
    ALTURA_TELA = TAMANHO_TABULEIRO + 40  # board + counter

    WHITE = (255, 255, 255)
    GRAY = (150, 150, 150)
    BLACK = (0, 0, 0)

    pygame.init()
    tela = pygame.display.set_mode((TAMANHO_TABULEIRO, ALTURA_TELA))
    pygame.display.set_caption('Problema das 8 rainhas - Hill Climbing')

    fonte = pygame.font.SysFont("Segoe UI Symbol", 64)
    fonte_contador = pygame.font.SysFont("Arial", 24)

    frame = 0
    clock = pygame.time.Clock()

    rodando = True
    while rodando:
        tela.fill(WHITE)

        for linha in range(N):
            for coluna in range(N):
                rect = pygame.Rect(coluna * TAMANHO_QUADRADO, linha * TAMANHO_QUADRADO, TAMANHO_QUADRADO, TAMANHO_QUADRADO)
                if (linha + coluna) % 2 == 0:
                    pygame.draw.rect(tela, GRAY, rect)
                else:
                    pygame.draw.rect(tela, WHITE, rect)

        estado = estados[frame]
        for coluna, linha in enumerate(estado):
            text = fonte.render(u'♛', True, BLACK)
            text_rect = text.get_rect(center=(
                coluna * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2,
                linha * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2
            ))
            tela.blit(text, text_rect)

        counter_text = fonte_contador.render(f"Estado {frame + 1} de {len(estados)}", True, BLACK)
        tela.blit(counter_text, (10, TAMANHO_TABULEIRO + 5))  # y = bottom of board + margin
        attack_text = fonte_contador.render(f"Ataques: {listaAtaques[frame]}", True, BLACK)
        tela.blit(attack_text, (500, TAMANHO_TABULEIRO + 5))

        pygame.display.flip()
        pygame.image.save(tela, "my_file"+str(frame)+".png")
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        pygame.time.delay(1500)
        if frame < len(estados) - 1:
            frame += 1
        else:
            pass

        clock.tick(60)

    pygame.quit()

# O estado inicial é um vetor prenchido com os numeros de 1 a 8 de forma aleatoria. O índice do vetor
# determina a coluna da rainha, e o seu valor determina a linha em que a rainha se encontra. 
estado = list(range(0, 8))
random.shuffle(estado)
estado = [0,0,0,0,0,0,0,0]
listaEstados = CalcularMelhorEstado(estado)
listaAtaques = list()
for x in listaEstados:
    listaAtaques.append(CalcularAtaques(x))

print("\n\n")

AnimarTabuleiro(listaEstados, listaAtaques)

