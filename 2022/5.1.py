tab = []
holder = open(0)

for line in holder:
    if line == "\n":
        break
    tab.append([line[i*4+1] for i in range(len(line) // 4)])

tab.pop()
tab = [list("".join(c).strip()[::-1]) for c in zip(*tab)]

for line in holder:
    a = int(line[line.find(" ")+1:line.find("from")-1])          # amount
    b = int(line[line.find("from")+5:line.find("to")-1]) - 1     # from
    c = int(line[line.rfind(" ")+1:]) - 1                        # to
    # print(a, b, c)
    for i in range(a):
        tab[c].append(tab[b][-1])
        tab[b].pop()

print(tab)
print("".join([i[-1] for i in tab]))
