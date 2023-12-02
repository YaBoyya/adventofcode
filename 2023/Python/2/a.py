def evaluate(groups):
    for group in groups:
        g = group.strip().split(', ')
        for color in g:
            col = color.split(" ")
            if int(col[0]) > 12 and col[1] == 'red':
                return False
            elif int(col[0]) > 13 and col[1] == 'green':
                return False
            elif int(col[0]) > 14 and col[1] == 'blue':
                return False
    return True


sum = 0
with open("2023/input/2.txt", "r") as f:
    for i, line in enumerate(f.readlines(), 1):
        line = line.strip().split(":")[-1]
        groups = line.split(";")
        if evaluate(groups):
            sum += i
print(sum)
