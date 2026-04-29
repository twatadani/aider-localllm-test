"""Module for Gomoku board operations."""
def create_board(size=10):
    """Create an empty Gomoku board."""
    return [['.' for _ in range(size)] for _ in range(size)]

def print_board(board, winning_line=None):
    """Print the Gomoku board with coordinates and highlight the winning line."""
    print('   ' + ' '.join(str(i) for i in range(len(board))))
    print('  ' + '-' * (2 * len(board) - 1))
    for i, row in enumerate(board):
        print(str(i) + ' |', end='')
        for j, cell in enumerate(row):
            if winning_line and (i, j) in winning_line:
                print('\033[42m' + cell + '\033[0m', end=' ')
            else:
                print(cell, end=' ')
        print()
    print()

def is_valid_move(board, row, col):
    """Check if a move is valid."""
    return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == '.'

def make_move(board, row, col, player):
    """Make a move on the board."""
    if is_valid_move(board, row, col):
        board[row][col] = player

def check_winner(board, player):
    """Check if a player has won and return the winning line."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == player:
                for k in range(5):
                    if i <= len(board)-5 and all(board[i+k][j] == player for k in range(5)):
                        winning_line = [(i+k, j) for k in range(5)]
                        return True, winning_line
                    if j <= len(board[0])-5 and all(board[i][j+k] == player for k in range(5)):
                        winning_line = [(i, j+k) for k in range(5)]
                        return True, winning_line
                    if i <= len(board)-5 and j <= len(board[0])-5 and all(board[i+k][j+k] == player for k in range(5)):
                        winning_line = [(i+k, j+k) for k in range(5)]
                        return True, winning_line
                    if i <= len(board)-5 and j >= 4 and all(board[i+k][j-k] == player for k in range(5)):
                        winning_line = [(i+k, j-k) for k in range(5)]
                        return True, winning_line
    return False, None
