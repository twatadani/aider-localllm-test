"""
Interactive Gomoku game between user and computer.
The board size is 10x10. The computer algorithm has three levels of strength: weak, normal, and strong.
"""
import sys
from gomoku_board import create_board, print_board, is_valid_move, make_move, check_winner
from gomoku_ai import weak_ai, normal_ai, strong_ai

def play_game():
    """Main function to run the game."""
    board = create_board()
    print("Welcome to Gomoku!")
    difficulty = input("Choose computer difficulty (weak, normal, strong): ")
    ai_move_func = weak_ai if difficulty == 'weak' else normal_ai if difficulty == 'normal' else strong_ai
    player = input("Do you want to go first (y/n)? ") == 'y'
    while True:
        print_board(board)
        if player:
            row, col = map(int, input("Enter your move (row and column): ").split())
            make_move(board, row, col, 'X')
        else:
            print("Computer's turn...")
            row, col = ai_move_func(board)
            make_move(board, row, col, 'O')
        if check_winner(board, 'X'):
            print("Congratulations! You won!")
            break
        elif check_winner(board, 'O'):
            print("Computer won! Better luck next time.")
            break
        elif all(board[i][j] != '.' for i in range(10) for j in range(10)):
            print("It's a draw!")
            break
        player = not player

if __name__ == '__main__':
    play_game()
