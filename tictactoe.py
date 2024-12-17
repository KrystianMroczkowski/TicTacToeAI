"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count, o_count, empty_count = 0, 0, 0

    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
            elif cell == EMPTY:
                empty_count += 1

    if x_count > o_count:
        return O
    return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for row_index, row in enumerate(board):
        for col_index, value in enumerate(row):
            if value == EMPTY:
                possible_actions.add((row_index, col_index))

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    current_player = player(board)
    possible_actions = actions(board)

    if action not in possible_actions:
        raise ValueError("The move is not valid.")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    if not actions(board):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_result = winner(board)

    if game_result == X:
        return 1
    elif game_result == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_value, best_move = max_value(board)
    elif current_player == O:
        best_value, best_move = min_value(board)
    else:
        return None

    return best_move

def max_value(board):
    if terminal(board):
        return utility(board), None

    available_actions = actions(board)
    best_value = -100
    best_move = None
    for action in available_actions:
        value, move = min_value(result(board, action))
        if best_value < value:
            best_value = value
            best_move = action

    return best_value, best_move

def min_value(board):
    if terminal(board):
        return utility(board), None

    available_actions = actions(board)
    best_value = 100
    best_move = None
    for action in available_actions:
        value, move = max_value(result(board, action))
        if best_value > value:
            best_value = value
            best_move = action

    return best_value, best_move
