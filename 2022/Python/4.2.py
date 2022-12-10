total = 0
for line in open(0):
    a = line[:line.find(",")]
    b = line[line.find(",")+1:]

    a = range(int(a[:a.find("-")]), int(a[a.find("-")+1:])+1)
    b = range(int(b[:b.find("-")]), int(b[b.find("-")+1:])+1)

    for i in a:
        if i in b:
            total += 1
            break

print(total)
