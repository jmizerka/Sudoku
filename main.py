import random
from typing import List, Tuple


def print_board(board: List[List[int]]) -> None:
    for i in range(len(board)):
        # Print horizontal separator after every 3 rows
        if i % 3 == 0 and i != 0:
            print('-' * 23)
        for j in range(len(board[0])):
            # Print vertical separator after every 3 columns
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            # Print the value in the cell
            print(str(board[i][j]) + ' ', end='')
        print('')


def check_if_possible(board: List[List[int]], num: int, indices: Tuple[int, int]) -> bool:
    x, y = indices[0] // 3, indices[1] // 3
    # Check the row, column, and the 3x3 square for the presence of the number
    row_check = board[indices[0]]
    col_check = [el[indices[1]] for el in board]
    square_check = [element for el in board[x * 3:(x + 1) * 3] for element in el[y * 3:(y + 1) * 3]]
    return num not in row_check and num not in col_check and num not in square_check


def find_empty(board: List[List[int]]) -> Tuple[int, int]:
    for i in range(len(board)):
        for j in range(len(board[0])):
            # Return indices of the first empty cell (value = 0)
            if board[i][j] == 0:
                return i, j


def solver(board: List[List[int]]) -> bool:
    indices = find_empty(board)
    num_list = list(range(1, 10))
    random.shuffle(num_list)
    # Base case: if no empty cells are found, the puzzle is solved
    if indices is None:
        return True
    for i in num_list:
        # Check if it's possible to place the current number at the empty position
        if check_if_possible(board, i, indices):
            board[indices[0]][indices[1]] = i
            # Recursively try to solve the updated board
            if solver(board):
                return True
            # If the current placement leads to an invalid solution, backtrack
            board[indices[0]][indices[1]] = 0
    return False


def remove_nums(board: List[List[int]], num: int):
    for i in range(num):
        x, y = random.randint(0, 8), random.randint(0, 8)
        board[x][y] = 0
    return board


if __name__ == '__main__':
    # Creating an empty Sudoku board
    su_board = [[0] * 9 for _ in range(9)]
    # Generating a solved Sudoku board
    solver(su_board)
    # Removing numbers to create a puzzle
    remove_nums(su_board, 40)
    # Printing the initial Sudoku board
    print('------SUDOKU BOARD-----\n')
    print_board(su_board)
    # Solving the Sudoku puzzle
    solver(su_board)
    # Printing the solved Sudoku board
    print('\n')
    print('------SOLVED BOARD-----\n')
    print_board(su_board)
