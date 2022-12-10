import numpy as np

total = []
tab = []
for line in open(0):
    tab.append([])
    tab[-1] = [int(x) for x in line[:-1]]
arr = np.array(tab)
height, width = arr.shape  # tuple <3
print(arr.shape)
for col in range(height):
    for row in range(width):
        L = U = R = D = 0
        for x in reversed(range(row)):
            if arr[col, row] > arr[col, x]:
                L += 1
                continue
            L += 1
            break
        for x in reversed(range(col)):
            if arr[col, row] > arr[x, row]:
                U += 1
                continue
            U += 1
            break
        for x in range(row+1, width):
            if arr[col, row] > arr[col, x]:
                R += 1
                continue
            R += 1
            break
        for x in range(col+1, height):
            if arr[col, row] > arr[x, row]:
                D += 1
                continue
            D += 1
            break
        print(L, U, R, D)
        total.append(L*U*R*D)


print(max(total))
