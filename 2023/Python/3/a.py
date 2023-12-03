input = open('2023/input/3.txt', 'r').readlines()

val = ''
flag = False
sum = 0
for r, line in enumerate(input):
    line = line.strip()
    for c, ch in enumerate(line):
        if ch.isdigit():
            val += ch
        if not ch.isdigit() and val != '' or c >= len(line) - 1:
            for cr in [r-1, r, r+1]:
                if cr < 0 or cr >= len(input):
                    continue
                c_start = c-len(val)-1 if c-len(val)-1 >= 0 else 0
                for cc in range(c_start, c+1):
                    if not input[cr][cc].isdigit() and input[cr][cc] != '.':
                        flag = True
            if flag is True:
                sum += int(val)
                flag = False
            val = ''
print(sum)
