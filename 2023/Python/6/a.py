time, distance = [list(map(int, line.split(':')[1].strip().split()))
                  for line in open("2023/input/6.txt").readlines()]

ans = 1

for t, d in zip(time, distance):
    margin = 0
    for i in range(t+1):
        if i * (t-i) > d:
            margin += 1
    ans *= margin

print(ans)
