"""Module for Gomoku AI algorithms."""
import random
import time
from gomoku_board import is_valid_move, make_move, check_winner

def weak_ai(board):
    """Weak AI algorithm for Gomoku."""
    while True:
        row, col = random.randint(0, 9), random.randint(0, 9)
        if is_valid_move(board, row, col):
            return row, col

def normal_ai(board):
    """Normal AI algorithm for Gomoku."""
    def score_move(row, col):
        """Calculate the score of a move."""
        score = 0
        for dr, dc in [(1, 0), (0, 1), (1, 1), (-1, 1)]:
            for player in ['X', 'O']:
                count = 0
                blocked = False
                for i in range(-4, 5):
                    r, c = row + dr * i, col + dc * i
                    if not is_valid_move(board, r, c):
                        blocked = True
                    elif board[r][c] == player:
                        count += 1
                if count >= 5:
                    score = float('inf') if player == 'O' else float('-inf')
                    break
                elif count > 0:
                    score += (1 << count) * (-1 if player == 'O' else 1)
                    if blocked:
                        score //= 2
        return score

    best_score = float('-inf')
    best_move = None
    for row in range(10):
        for col in range(10):
            if is_valid_move(board, row, col):
                make_move(board, row, col, 'O')
                score = score_move(row, col)
                board[row][col] = '.'
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

def strong_ai(board, time_limit=15):
    """Strong AI algorithm for Gomoku using minimax with alpha-beta pruning and time limit."""
    def evaluate(board, player):
        """Evaluate the score of a board state."""
        score = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == player:
                    for k in range(5):
                        if i <= len(board)-5 and all(board[i+k][j] == player for k in range(5)):
                            score += 10 ** (k+1)
                        if j <= len(board[0])-5 and all(board[i][j+k] == player for k in range(5)):
                            score += 10 ** (k+1)
                        if i <= len(board)-5 and j <= len(board[0])-5 and all(board[i+k][j+k] == player for k in range(5)):
                            score += 10 ** (k+1)
                        if i <= len(board)-5 and j >= 4 and all(board[i+k][j-k] == player for k in range(5)):
                            score += 10 ** (k+1)
        return score

    def minimax(board, depth, alpha, beta, maximizing_player):
        """Minimax algorithm with alpha-beta pruning."""
        winner, _ = check_winner(board, 'X')
        if depth == 0 or winner:
            return evaluate(board, 'O' if maximizing_player else 'X')
        if maximizing_player:
            max_eval = float('-inf')
            for row in range(10):
                for col in range(10):
                    if is_valid_move(board, row, col):
                        make_move(board, row, col, 'O')
                        eval = minimax(board, depth-1, alpha, beta, False)
                        board[row][col] = '.'
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
                if time.time() - start_time >= time_limit:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for row in range(10):
                for col in range(10):
                    if is_valid_move(board, row, col):
                        make_move(board, row, col, 'X')
                        eval = minimax(board, depth-1, alpha, beta, True)
                        board[row][col] = '.'
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
                if time.time() - start_time >= time_limit:
                    break
            return min_eval

    best_score = float('-inf')
    best_move = None
    start_time = time.time()
    for row in range(10):
        for col in range(10):
            if is_valid_move(board, row, col):
                make_move(board, row, col, 'O')
                score = minimax(board, 4, float('-inf'), float('inf'), False)
                board[row][col] = '.'
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
            if time.time() - start_time >= time_limit:
                break
    return best_move
