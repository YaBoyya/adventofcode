total = 0
for line in open(0):
    x = len(line)/2

    a = line[:int(x)]
    b = line[int(x):]
    hold = ""
    for letter in a:
        if b.find(letter) != -1:
            hold = b[b.find(letter)]
            break

    if hold.islower():
        total += ord(hold) - 97 + 1
    elif hold.isupper():
        total += ord(hold) - 65 + 27
print(total)
