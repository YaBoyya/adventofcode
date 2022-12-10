line = input()
hold = line[:14]
for i in range(14, len(line)):
    if len(set(hold)) >= 14:
        print(i)
        break
    else:
        hold = hold[1:]
        hold += line[i]
