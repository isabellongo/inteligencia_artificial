

# Primeiro, definir como elas serao representadas 
# Gerar aleatoriamente a posicao inicial
# Calcular os ataques
# Iterativamente, de rainha em rainha, gera uma vizinhanca, 
# e assim que encontrar um valor menor de ataques, ela muda o estado
# se nao encontrar um valor menor de ataques, para o algoritmo (ou em ataques = 0)

import random

# Essa funcao calcula quantos ataques existem no tabuleiro, como as rainhas estao sempre na mesma coluna,
# ele verifica se elas estao na mesma linha ou na mesma diagonal.
def CalcularAtaques(estado):
    ataques = 0
    for i in range(len(estado)):
        for j in range(i+1, len(estado)):
            if(estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j)):
                ataques = ataques + 1
    return ataques

def TestarVizinhos(estado): 
    estadonovo = estado.copy()
    ataques = CalcularAtaques(estado)
    for i in range(len(estado)):
        for j in range(len(estado)):
            estadonovo[i] = j
            if CalcularAtaques(estadonovo) < ataques:
                print("encontrou")
                return estadonovo
            estadonovo[i]=estado[i]
    return estado

#def CalcularMelhorEstado(): 
#    estado

# O estado inicial é um vetor prenchido com os numeros de 1 a 8 de forma aleatoria. O índice do vetor
# determina a coluna da rainha, e o seu valor determina a linha em que a rainha se encontra. 
estado = list(range(0, 8))
random.shuffle(estado)
print(estado)
print(CalcularAtaques(estado))

estadomelhor = TestarVizinhos(estado)
print(estadomelhor)
print(CalcularAtaques(estadomelhor))
