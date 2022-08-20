from xmlrpc.client import Boolean
import pygame, sys
import numpy as np

pygame.init()

#Sizes for objects
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

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

#pygame.draw.line(screen, RED, (10, 10), (300, 300), 10)

def drawLines():
    #First Horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT/3), (WIDTH, HEIGHT/3), LINE_WIDTH)
    #Second Horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 2*HEIGHT/3), (WIDTH, 2*HEIGHT/3), LINE_WIDTH)

    #First Veritcal
    pygame.draw.line(screen, LINE_COLOR, (WIDTH/3, 0), (WIDTH/3, HEIGHT), LINE_WIDTH)
    #Second Veritcal
    pygame.draw.line(screen, LINE_COLOR, (2*WIDTH/3, 0), (2*WIDTH/3, HEIGHT), LINE_WIDTH)

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
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)
drawLines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clickedRow = int(mouseY // 200)
            clickedCol = int(mouseX // 200)

            if avaliableSquare(clickedRow, clickedCol):
                if player == 1:
                    markSquare(clickedRow, clickedCol, player)
                    player = 2
                elif player == 2:
                    markSquare(clickedRow, clickedCol, player)
                    player = 1
                
                drawFigures()
    pygame.display.update()