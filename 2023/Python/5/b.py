# With the help of Hyper Neutrino:
# https://github.com/hyper-neutrino/advent-of-code
inputs, *blocks = open("2023/input/5.txt", "r").read().split("\n\n")

inputs = list(map(int, inputs.split(": ")[-1].split()))

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i]+inputs[i+1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    new = []
    while len(seeds) > 0:
        s, e = seeds.pop()

        for start, source, length in ranges:
            overlap_s = max(s, source)
            overlap_e = min(e, source + length)
            if overlap_s < overlap_e:
                new.append((overlap_s - source + start,
                            overlap_e - source + start))
                if overlap_s > s:
                    seeds.append((s, overlap_s))
                if e > overlap_e:
                    seeds.append((overlap_e, e))
                break
        else:
            new.append((s, e))
    seeds = new
print(min(seeds))
