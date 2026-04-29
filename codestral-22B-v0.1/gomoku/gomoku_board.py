"""Module for Gomoku board operations."""
def create_board(size=10):
    """Create an empty Gomoku board."""
    return [['.' for _ in range(size)] for _ in range(size)]

def print_board(board):
    """Print the Gomoku board with coordinates."""
    print('   ' + ' '.join(str(i) for i in range(len(board))))
    print('  ' + '-' * (2 * len(board) - 1))
    for i, row in enumerate(board):
        print(str(i) + ' |' + ' '.join(row))
    print()

def is_valid_move(board, row, col):
    """Check if a move is valid."""
    return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == '.'

def make_move(board, row, col, player):
    """Make a move on the board."""
    if is_valid_move(board, row, col):
        board[row][col] = player

def check_winner(board, player):
    """Check if a player has won."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == player and
                ((all(board[i+k][j] == player for k in range(5)) if i <= len(board)-5 else False) or
                 (all(board[i][j+k] == player for k in range(5)) if j <= len(board[0])-5 else False) or
                 (all(board[i+k][j+k] == player for k in range(5)) if i <= len(board)-5 and j <= len(board[0])-5 else False) or
                 (all(board[i+k][j-k] == player for k in range(5)) if i <= len(board)-5 and j >= 4 else False))):
                return True
    return False
