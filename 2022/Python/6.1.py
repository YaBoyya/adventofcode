line = input()
hold = line[:4]
for i in range(4, len(line)):
    if len(set(hold)) >= 4:
        print(i)
        break
    else:
        hold = hold[1:]
        hold += line[i]
