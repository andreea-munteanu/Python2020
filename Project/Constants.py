import numpy as np


with open('4inaROW.txt', 'r') as file :
    content = file.read()
    OPPONENT, ROWS, COLS, FIRST_PLAYER = content.split()
    ROWS, COLS = int(ROWS), int(COLS)
    # print("OPPONENT =", OPPONENT, ', ROWS = ', ROWS, ', COLS = ', COLS, ', FIRST PLAYER = ', FIRST_PLAYER)
    assert ROWS >= 4 and COLS >= 4, 'Board must be at least 4x4.'
file.close()

# screen dimensions
WIDTH = ROWS * 50
HEIGHT = WIDTH * 50
SQUARE_SIZE = 50

# virtual board
board = np.zeros((ROWS, COLS)) # at first board is free

# moving directions
N, NE, E, SE, S, SW, W, NW = 0, 1, 2, 3, 4, 5, 6, 7
direction = [N, NE, E, SE, S, SW, W, NW]
GO_DIR = {N : (-1, 0),
          NE : (-1, 1),
          E : (0, 1),
          SE : (1, 1),
          S : (1, 0),
          SW : (1, -1),
          W : (0, -1),
          NW : (-1, -1)}
