import numpy as np


def t_move(head):
    for i in range(9):
        dif = np.subtract(head[i], head[i+1])
        if any(np.abs(dif) == 2):
            head[i+1] = np.add(head[i+1], np.sign(dif))
    return head

def addition(head, vec):
    for i in range(10):
        head[i] = np.add(head[i], vec)
    return head



directions = {"L": (0, -1), "U": (-1, 0), "R": (0, 1), "D": (1, 0)}  # [x, y]
N = 5  # rows
M = 5  # cols
arr = np.zeros([N, M])

total = 0
H = [[4, 0] for x in range(10)]# y, x

for line in open(0):
    direc = line[0]
    amt = line[2:]
    for i in range(int(amt)):
        H[0] = np.add(H[0], directions[direc])
        if H[0][0] >= N:       # down
            arr = np.append(arr, np.zeros([1, M]), axis=0)
            N += 1
        elif H[0][0] <= 0:     # up
            arr = np.append(np.zeros([1, M]), arr, axis=0)
            N += 1
            H = addition(H, [1, 0])
        elif H[0][1] >= M:     # right
            arr = np.append(arr, np.zeros([N, 1]), axis=1)
            M += 1
        elif H[0][1] <= 0:     # left
            arr = np.append(np.zeros([N, 1]), arr, axis=1)
            M += 1
            H = addition(H, [0, 1])
        H = t_move(H)
        if arr[H[9][0], H[9][1]] == 0:
            total += 1
            arr[H[9][0], H[9][1]] = 1
        # print(H, end="***********\n")
print(total)
# for y in range(N):
#     for x in range(M):
#         print(str(arr[y][x]).replace('0', '.').replace('1', '#'), end="")
#     print(end="\n")