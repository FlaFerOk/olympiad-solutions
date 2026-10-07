knights_moves = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

def number_of_tracks(y, x):
    count = 0
    for move in knights_moves:
        if 0 <= y + move[0] < N and 0 <= x + move[1] < N:
            if chessboard[y + move[0]][x + move[1]] == -1:
                count += 1
    return count


def serch_moves(y, x):
    moves = []
    for move in knights_moves:
        if 0 <= y + move[0] < N and 0 <= x + move[1] < N:
            if 0 <= y + move[0] < N and 0 <= x + move[1] < N and chessboard[y + move[0]][x + move[1]] == -1:
                moves.append([y + move[0], x + move[1], number_of_tracks(move[0] + y, move[1] + x)])
    moves.sort(key=lambda row: row[2])
    return moves


def knights_way(y, x, step):
    chessboard[y][x] = step
    if step == N * N:
        return True
    moves = serch_moves(y, x)
    if not moves:
        return False
    return knights_way(moves[0][0], moves[0][1], step + 1)


N, a, b = map(int, input().split(','))
chessboard = table = [[-1] * N for _ in range(N)]

if knights_way(b, a, 1):
    for line in chessboard:
        print(''.join(f'{x:4}' for x in line))
else:
    print("nenasiel")