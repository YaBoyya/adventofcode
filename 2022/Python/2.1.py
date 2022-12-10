# A/X for Rock -> 1 point
# B/Y for Paper -> 2 points
# C/Z for Scissors -> 3 points
# win -> 6 points
# draw -> 3 points
# lose -> 0 points
total = 0

while 1:
    try:
        line = input()
    except:
        break

    if line[2] == "X":
        total += 1
    elif line[2] == "Y":
        total += 2
    elif line[2] == "Z":
        total += 3

    if line == "A X" or line == "B Y" or line == "C Z":
        total += 3
    elif line == "C X" or line == "A Y" or line == "B Z":
        total += 6

print(total)


