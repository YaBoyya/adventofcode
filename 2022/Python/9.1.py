import numpy as np


def t_move(head, tail):
    dif = head - tail
    if any(np.abs(dif) == 2):
        tail += np.sign(dif)
    return tail


directions = {"L": (0, -1), "U": (-1, 0), "R": (0, 1), "D": (1, 0)}  # [x, y]
N = 5  # rows
M = 5  # cols
arr = np.zeros([N, M])

total = 0
H = T = [4, 0]  # y, x
for line in open(0):
    direc = line[0]
    amt = line[2:]
    for i in range(int(amt)):
        H = np.add(H, directions[direc])
        if H[0] >= N:       # down
            arr = np.append(arr, np.zeros([1, M]), axis=0)
            N += 1
        elif H[0] <= 0:     # up
            arr = np.append(np.zeros([1, M]), arr, axis=0)
            N += 1
            T = np.add(T, [1, 0])
            H = np.add(H, [1, 0])
        elif H[1] >= M:     # right
            arr = np.append(arr, np.zeros([N, 1]), axis=1)
            M += 1
        elif H[1] <= 0:     # left
            arr = np.append(np.zeros([N, 1]), arr, axis=1)
            M += 1
            T = np.add(T, [0, 1])
            H = np.add(H, [0, 1])
        T = t_move(H, T)
        if arr[T[0], T[1]] == 0:
            total += 1
            arr[T[0], T[1]] = 1
print(total)