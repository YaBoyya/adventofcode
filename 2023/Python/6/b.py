time, distance = [int(''.join(line.split(':')[1].strip().split()))
                  for line in open("2023/input/6.txt").readlines()]

print(time, distance)

ans = 0
for i in range(time):
    if i * (time-i) > distance:
        ans += 1

print(ans)
