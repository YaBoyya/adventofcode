input = open('2023/input/3.txt', 'r').readlines()

val = ''
ratio = []
sum = 0
for r, line in enumerate(input):
    line = line.strip()
    for c, ch in enumerate(line):
        if ch == "*":
            for cr in [r-1, r, r+1]:
                for cc in [c-1, c, c+1]:
                    if (cr < 0 or cr >= len(input) or cc < 0
                            or cc >= len(line) or not input[cr][cc].isdigit()):
                        continue
                    val = input[cr][cc]
                    i = 1
                    while input[cr][cc-i].isdigit():
                        val = input[cr][cc-i] + val
                        i += 1
                    i = 1
                    while input[cr][cc+i].isdigit():
                        val += input[cr][cc+i]
                        i += 1
                    if val != '' and int(val) not in ratio:
                        ratio.append(int(val))
                    val = ''
        if len(ratio) > 1:
            res = 1
            for i in ratio:
                res *= i
            sum += res
        ratio = []
print(sum)
