import numpy as np

total = 0
tab = []
for line in open(0):
    tab.append([])
    tab[-1] = [int(x) for x in line[:-1]]
arr = np.array(tab)
height, width = arr.shape  # tuple <3
print(arr.shape)
for col in range(height):
    for row in range(width):
        if col == 0 or row == 0 or col == height-1 or row == width-1:
            total += 1
        elif all(arr[col, row] > arr[col, x] for x in range(row)):  # left
            total += 1
        elif all(arr[col, row] > arr[x, row] for x in range(col)):  # up
            total += 1
        elif all(arr[col, row] > arr[col, x] for x in range(row+1, width)):  # right
            total += 1
        elif all(arr[col, row] > arr[x, row] for x in range(col+1, height)):  # down
            total += 1

print(total)
