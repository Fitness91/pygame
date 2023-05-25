
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Tic-Tac-Toe")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the game board
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

# Set up the players
players = ['X', 'O']
current_player = 0

# Set up the fonts
font = pygame.font.Font(None, 80)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Get the position of the mouse click
            pos = pygame.mouse.get_pos()
            col = pos[0] // 100
            row = pos[1] // 100

            # Update the game board if the clicked position is valid
            if board[row][col] == '':
                board[row][col] = players[current_player]
                current_player = (current_player + 1) % 2

    # Render graphics
    screen.fill(WHITE)

    # Draw the game board
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(screen, BLACK, (col * 100, row * 100, 100, 100), 2)
            text = font.render(board[row][col], True, BLACK)
            screen.blit(text, (col * 100 + 35, row * 100 + 20))

    # Check for a winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            pygame.draw.line(screen, BLACK, (0, row * 100 + 50), (300, row * 100 + 50), 3)
            pygame.display.flip()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            pygame.draw.line(screen, BLACK, (col * 100 + 50, 0), (col * 100 + 50, 300), 3)
            pygame.display.flip()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

    if board[0][0] == board[1][1] == board[2][2] != '':
        pygame.draw.line(screen, BLACK, (50, 50), (250, 250), 3)
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    if board[0][2] == board[1][1] == board[2][0] != '':
        pygame.draw.line(screen, BLACK, (250, 50), (50, 250), 3)
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    pygame.display.flip()
