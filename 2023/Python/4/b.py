f = open('2023/input/4.txt', 'r').readlines()
instances = [1 for _ in range(len(f))]

for i, line in enumerate(f):
    t = line.split(":")
    vals = t[-1].strip().split(' | ')
    winning = vals[0].split(" ")
    nums = vals[-1].split(" ")
    win_cnt = 0
    for win in winning:
        if win in nums and win != '':
            win_cnt += 1
    for j in range(1, win_cnt+1):
        instances[i+j] += (1*instances[i])
print(instances)
print(sum(instances))
