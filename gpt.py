import pygame
import time

# Tamanho do tabuleiro
N = 8
TILE_SIZE = 80
SCREEN_SIZE = N * TILE_SIZE

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)

def draw_board(screen, board):
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 60)
    for row in range(N):
        for col in range(N):
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, GRAY, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            if board[row][col] == 1:
                text = font.render('♛', True, RED)
                screen.blit(text, (col * TILE_SIZE + 15, row * TILE_SIZE + 10))
    pygame.display.flip()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(screen, board, col):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            draw_board(screen, board)
            time.sleep(0.5)  # Pausa para ver a animação

            if solve_n_queens(screen, board, col + 1):
                return True

            board[i][col] = 0  # Backtrack
            draw_board(screen, board)
            time.sleep(0.5)
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption('Problema das 8 Rainhas Animado')

    board = [[0 for _ in range(N)] for _ in range(N)]

    running = True
    solving = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not solving:
            solving = True
            solve_n_queens(screen, board, 0)

    pygame.quit()

if __name__ == "__main__":
    main()
