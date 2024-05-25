import random
import pandas as pd
from typing import List, Optional

def get_board_as_string(board: List[List[str]]) -> str:
    """
    Display function for board
    """
    return '\n'.join([' | '.join(row) + '\n' + '-' * 9 for row in board])

def print_board(board: List[List[str]]):
    print(get_board_as_string(board))

def check_winner(board: List[List[str]]) -> Optional[str]:
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def is_draw(board: List[List[str]]) -> bool:
    """
    Check if the game is a draw, AKA there are no empty spaces left
    """
    if check_winner(board):
        return False # If there is a winner, the game can't be a draw
    for row in board:
        if ' ' in row:
            return False
    return True

def evaluate_board(board: List[List[str]]) -> str:
    winner = check_winner(board)
    if winner:
        return winner
    elif is_draw(board):
        return 'Draw'
    else:
        return 'N/A'
    
def random_tic_tac_toe_board() -> List[List[str]]:
    choices = ['X', 'O', ' ']
    board = [[random.choice(choices) for _ in range(3)] for _ in range(3)]
    return board

def generate_data() -> None:
    # Generate 1000 boards and save them to file as 'board' and 'winner'
    boards = [random_tic_tac_toe_board() for _ in range(1000)]
    winners = [evaluate_board(board) for board in boards]

    df = pd.DataFrame({'board': boards, 'winner': winners})
    df.to_csv('tic_tac_toe_boards.csv', index=False)