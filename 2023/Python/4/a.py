ans = 0
for line in open('2023/input/4.txt', 'r').readlines():
    t = line.split(":")
    vals = t[-1].strip().split(' | ')
    winning = vals[0].split(" ")
    nums = vals[-1].split(" ")
    win_cnt = 0
    for win in winning:
        if win in nums and win != '':
            win_cnt += 1
    if win_cnt > 0:
        ans += (2**(win_cnt-1))
print(ans)
