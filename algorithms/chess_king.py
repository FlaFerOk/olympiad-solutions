from collections import deque

def find_a_way(S):
    queue = deque([S])
    steps = [[[999, 0, 0] for _ in range(8)] for _ in range(8)]
    steps[S[0]][S[1]][0] = 0
    while queue:
        step = queue.popleft()
        step_number = steps[step[0]][step[1]][0] + 1
        for y in range(-1, 2):
            y += step[0]
            for x in range(-1, 2):
                x += step[1]
                if y == step[0] and x == step[1]:
                    continue
                if 0 <= x < 8 and 0 <= y < 8:
                    if steps[y][x][0] > step_number:
                        steps[y][x] = [step_number, step[0], step[1]]
                        queue.append([y, x])
    return steps

S = input()
F = input()
S = [8 - int(S[1:]), ord(S[0]) - 97]
F = [8 - int(F[1:]), ord(F[0]) - 97]
moves = find_a_way(S)
while F[0] != S[0] and F[1] != S[1]:
    F = moves[F[0]][F[1]]
    print("L" if F[1] - S[1] > 0 else "R" )

