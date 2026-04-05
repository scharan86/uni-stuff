import math

HUMAN = 'X'
COMPUTER = 'O'
EMPTY = ' '

def print_board(board):
    for i in range(3):
        print(board[i*3], board[i*3+1], board[i*3+2])

def check_winner(board, player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[c] == player for c in line) for line in wins)

def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]

def is_terminal(board):
    return check_winner(board, HUMAN) or check_winner(board, COMPUTER) or not get_empty_cells(board)

def minimax(board, is_maximising):
    if check_winner(board, COMPUTER): return 1
    if check_winner(board, HUMAN): return -1
    if not get_empty_cells(board): return 0
    if is_maximising:
        best = -math.inf
        for cell in get_empty_cells(board):
            board[cell] = COMPUTER
            best = max(best, minimax(board, False))
            board[cell] = EMPTY
        return best
    else:
        best = math.inf
        for cell in get_empty_cells(board):
            board[cell] = HUMAN
            best = min(best, minimax(board, True))
            board[cell] = EMPTY
        return best

def computer_move(board):
    best_score = -math.inf
    best_cell = None
    for cell in get_empty_cells(board):
        board[cell] = COMPUTER
        score = minimax(board, False)
        board[cell] = EMPTY
        if score > best_score:
            best_score = score
            best_cell = cell
    board[best_cell] = COMPUTER

def human_move(board):
    while True:
        try:
            move = int(input("move (1-9): ")) - 1
            if move in get_empty_cells(board):
                board[move] = HUMAN
                break
        except ValueError:
            pass

def play():
    board = [EMPTY] * 9
    for turn in range(9):
        if is_terminal(board): break
        human_move(board) if turn % 2 == 0 else computer_move(board)
        print_board(board)
    if check_winner(board, HUMAN): print("you win")
    elif check_winner(board, COMPUTER): print("computer wins")
    else: print("draw")

if __name__ == '__main__':
    play()
