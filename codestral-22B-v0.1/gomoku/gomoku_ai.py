"""Module for Gomoku AI algorithms."""
import random

def weak_ai(board):
    """Weak AI algorithm for Gomoku."""
    while True:
        row, col = random.randint(0, 9), random.randint(0, 9)
        if is_valid_move(board, row, col):
            return row, col

def normal_ai(board):
    """Normal AI algorithm for Gomoku."""
    # TODO: Implement normal AI algorithm
    pass

def strong_ai(board):
    """Strong AI algorithm for Gomoku."""
    # TODO: Implement strong AI algorithm
    pass
