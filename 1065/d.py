import math
from operator import itemgetter

closest_cells = (1, 2)


def horse_move(start_i, start_j, i, j, n):
    if n == 3:
        if (i == 1 and j == 1) or (start_i == 1 and start_j == 1):
            return 1000
        if (i == 1 and start_i == 1) or (j == 1 and start_j == 1):
            return 4

    i -= start_i
    j -= start_j
    i = abs(i)
    j = abs(j)
    if start_i not in [0, n-1] or start_j not in [0, n-1]:
        delta = i - j
        if j > delta:
            return delta - 2 * math.floor((delta - j) / 3)
        else:
            return delta - 2 * math.floor((delta - j) / 4)
    if (i == j) and (j in closest_cells):
        return 4
    if (i + j) == 1:
        return 3
    biggest_div = max(i // 2, j // 2, (i + j) // 3)
    return int(biggest_div + ((biggest_div + i + j) % 2))


def bishop_move(start_i, start_j, i, j):
    if (start_i + start_j) % 2 != (i + j) % 2:
        return 1000
    if abs(start_i - i) == abs(start_j - j):
        return 1
    return 2


def rook_move(start_i, start_j, i, j):
    if start_i == i or start_j == j:
        return 1
    else:
        return 2


n = int(input())
desk = tuple(tuple(map(int, input().split())) for i in range(n))
moves = sorted(((desk[i][j], (i, j)) for i in range(n) for j in range(n)), key=itemgetter(0))
print(moves)
move_weights_per_figure = []
horse_moves = [horse_move(moves[i-1][1][0], moves[i-1][1][1], move[1][0], move[1][1], n) for i, move in enumerate(moves[1:], 1)]
bishop_moves = [bishop_move(moves[i-1][1][0], moves[i-1][1][1], move[1][0], move[1][1]) for i, move in enumerate(moves[1:], 1)]
rook_moves = [rook_move(moves[i-1][1][0], moves[i-1][1][1], move[1][0], move[1][1]) for i, move in enumerate(moves[1:], 1)]
print(horse_moves)
print(bishop_moves)
print(rook_moves)
