from xmlrpc.client import Boolean
import pygame, sys
import numpy as np

pygame.init()

#Sizes for objects
WIDTH = 800
HEIGHT = 800
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH //BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE//4

#Colors
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

#board 

board = np.zeros((BOARD_ROWS, BOARD_COLS))

player = 1
gameOver = False
#pygame.draw.line(screen, RED, (10, 10), (300, 300), 10)

def drawLines():
    #First Horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    #Second Horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 2*SQUARE_SIZE), (WIDTH, 2*SQUARE_SIZE), LINE_WIDTH)

    #First Veritcal
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    #Second Veritcal
    pygame.draw.line(screen, LINE_COLOR, (2*SQUARE_SIZE, 0), (2*SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def markSquare(row, col, player):
    board[row][col] = player

def avaliableSquare(row, col):
    return board[row][col] == 0

def isBoardFull():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def drawFigures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), int(row * SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def check_win(player):
    #vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col)
            return True
    
    #horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row)
            return True

    #asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal()
        return True

    #dsc disgonal win check 
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_dsc_diagonal()
        return True

def draw_vertical_winning_line(col):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2
    pygame.draw.line(screen, RED, (posX, 0), (posX, HEIGHT), 15)

def draw_horizontal_winning_line(row):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2
    pygame.draw.line(screen, RED, (0, posY), (WIDTH, posY), 15)

def draw_asc_diagonal():
    pygame.draw.line(screen, RED, (15, HEIGHT-15), (WIDTH - 15, 15), 15)

def draw_dsc_diagonal():
    pygame.draw.line(screen, RED, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

def restart():
    screen.fill(BG_COLOR)
    drawLines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


drawLines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clickedRow = int(mouseY // SQUARE_SIZE)
            clickedCol = int(mouseX // SQUARE_SIZE)

            if avaliableSquare(clickedRow, clickedCol):
                markSquare(clickedRow, clickedCol, player)
                if check_win(player):
                    gameOver = True
                player = player % 2 + 1
                
                drawFigures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                gameOver = False
                player = 1
    pygame.display.update()