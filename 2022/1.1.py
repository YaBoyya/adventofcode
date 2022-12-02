tab = [0]

while 1:
    try:
        cal = input()
    except:
        break
    if cal == "":
        tab.append(0)
        continue
    tab[-1] += int(cal)
print(max(tab))
