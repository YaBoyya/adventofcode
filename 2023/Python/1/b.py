words = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9')
    ]

sum = 0

with open("2023/input/1.txt", "r") as f:
    for line in f.readlines():
        digits = []

        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)

            for key, num in words:
                if line[i:].startswith(key):
                    digits.append(num)

        val = int(digits[0]+digits[-1])
        sum += val

print(sum)
