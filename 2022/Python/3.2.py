total = 0
while 1:
    try:
        a = input()
        b = input()
        c = input()
    except:
        break

    hold = ""

    for letter in a:
        if b.find(letter) != -1:
            hold = letter
            if c.find(hold) != -1:
                break

    if hold.islower():
        total += ord(hold) - 97 + 1
    elif hold.isupper():
        total += ord(hold) - 65 + 27
print(total)
