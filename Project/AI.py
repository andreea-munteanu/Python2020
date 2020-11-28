from Constants import ROWS, GO_DIR, board


def is_valid_location(board, col) :
    # column is valid if at least one cell (on line 0) is free
    return board[0][col] == 0

# return last free row on column col
def get_next_free_row(board, col):
    for row in range(ROWS):
        if board[row][col] == 0:
            return row

def get_column(): # at mouse click
    if pygame.mouse.get_pressed()[0] and mysprite.rect.collidepoint(pygame.mouse.get_pos()) :
        pass

def get_all_moves(pos): # pos = (row, col)
    moves = []
    row, col = pos
    # parse all neighbours, N to NW (clockwise)
    for dir in GO_DIR:
        new_x = x + GO_DIR[dirr][1]
        new_y = y + GO_DIR[dirr][0]
        print("neighbour: (", new_x, ",", new_y, ")")
        # check if neighbour within bounds:
        if is_valid_location(new_x, new_y) :
            # move from (x, y) to (new_x, new_y)
            move = (x, y, new_x, new_y)
            print(move)
            moves.append(move)
    return moves

print(get_all_moves((3,0)))