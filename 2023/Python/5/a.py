f = open("2023/input/5.txt", "r")

seeds = list(map(int, f.readline().strip().split(": ")[-1].split()))
step_seeds = []

for line in f.readlines():
    line = line.strip()

    if not line:
        continue

    if not line[0].isdigit():
        step_seeds = seeds[:]
        continue

    start, source, length = map(int, line.split())

    for i, seed in enumerate(seeds):
        if seed not in step_seeds:
            continue

        if seed >= source and seed <= source + length:
            seeds[i] += (start-source)

print(min(seeds))
