def evaluate(groups):
    r_min = 0
    g_min = 0
    b_min = 0
    for group in groups:
        g = group.strip().split(', ')
        for color in g:
            col = color.split(" ")
            if col[1] == 'red':
                r_min = max(int(col[0]), r_min)
            elif col[1] == 'green':
                g_min = max(int(col[0]), g_min)
            elif col[1] == 'blue':
                b_min = max(int(col[0]), b_min)
    return r_min * g_min * b_min


sum = 0
with open("2023/input/2.txt", "r") as f:
    for i, line in enumerate(f.readlines(), 1):
        line = line.strip().split(":")[-1]
        groups = line.split(";")
        sum += evaluate(groups)
print(sum)
