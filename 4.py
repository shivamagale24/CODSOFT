def is_safe(row, col, cols, diag1, diag2):

    if cols[col]:
        return False

    if diag1[row - col]:
        return False

    if diag2[row + col]:
        return False

    return True


def solve(row, n, board, cols, diag1, diag2):

    if row == n:
        for r in board:
            print(r)
        print("______________________")
        return

    for col in range(n):

        if is_safe(row, col, cols, diag1, diag2):

            board[row][col] = 1
            cols[col] = True
            diag1[row - col] = True
            diag2[row + col] = True

            solve(row + 1, n, board, cols, diag1, diag2)

            # Backtracking
            board[row][col] = 0
            cols[col] = False
            diag1[row - col] = False
            diag2[row + col] = False


def n_queens(n):

    board = [[0] * n for _ in range(n)]

    cols = [False] * n

    diag1 = {}
    diag2 = {}

    for i in range(-n, n):
        diag1[i] = False

    for i in range(2 * n):
        diag2[i] = False

    solve(0, n, board, cols, diag1, diag2)


n =4
n_queens(n)