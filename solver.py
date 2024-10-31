def get_subgrid_size(size):
    # Define subgrid dimensions based on board size
    if size == 4:
        return 2, 2
    elif size == 5:
        return 1, 5
    elif size == 6:
        return 2, 3
    elif size == 7:
        return 1, 7
    elif size == 9:
        return 3, 3
    elif size == 12:
        return 3, 4
    elif size == 16:
        return 4, 4
    elif size == 25:
        return 5, 5
    else:
        raise ValueError("Unsupported grid size.")

def is_valid(board, row, col, num, size):
    # Check if num is in the given row or column
    for i in range(size):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check within the subgrid
    subgrid_row, subgrid_col = get_subgrid_size(size)
    start_row, start_col = (row // subgrid_row) * subgrid_row, (col // subgrid_col) * subgrid_col

    for i in range(subgrid_row):
        for j in range(subgrid_col):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board, size):
    empty = find_empty(board, size)
    if not empty:
        return True

    row, col = empty
    for num in range(1, size + 1):
        if is_valid(board, row, col, num, size):
            board[row][col] = num
            if solve_sudoku(board, size):
                return True
            board[row][col] = 0

    return False

def find_empty(board, size):
    for row in range(size):
        for col in range(size):
            if board[row][col] == 0:
                return row, col
    return None
