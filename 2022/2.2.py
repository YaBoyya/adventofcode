# A for Rock -> 1 point
# B for Paper -> 2 points
# C for Scissors -> 3 points
# win -> 6 points
# draw -> 3 points
# lose -> 0 points
# X -> lose
# Y -> draw
# Z -> win
total = 0

while 1:
    try:
        line = input()
    except:
        break

    if line[2] == "Z":  # win
        total += 6
        if line[0] == "A":
            total += 2
        elif line[0] == "B":
            total += 3
        elif line[0] == "C":
            total += 1
    elif line[2] == "Y":  # draw
        total += 3
        if line[0] == "A":
            total += 1
        elif line[0] == "B":
            total += 2
        elif line[0] == "C":
            total += 3
    elif line[2] == "X":  # lose
        if line[0] == "A":
            total += 3
        elif line[0] == "B":
            total += 1
        elif line[0] == "C":
            total += 2
print(total)
