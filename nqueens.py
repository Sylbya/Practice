from collections import namedtuple

n = int(input("N= "))
board = [[False for _ in range(n)] for _ in range(n)]
Point = namedtuple("Point", ['x', 'y'])


def get_moves(point, size):
    if not point or not size:
        return
    id = point.x - point.y
    jd = size - point.x - 1 - point.y
    for i in range(size):
        for j in range(size):
            if Point(i, j) != point\
                    and (i == j + id or j == size - i - 1 - jd or point.x == i or point.y == j):
                yield Point(i, j)


def is_safe(pos, board):
    return all(not board[p.x][p.y] for p in get_moves(pos, len(board)))


def solve(board, cur_col):
    if len(board) <= cur_col:
        return True
    for row in range(len(board)):
            if is_safe(Point(row, cur_col), board):
                board[row][cur_col] = True
                if solve(board, cur_col + 1):
                    return True
                board[row][cur_col] = False


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print("{0} ".format("Q" if board[i][j] else "-"), end='')
        print()


solve(board, 0)
print_board(board)