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
three = 0
for i in range(3):
    three += max(tab)
    tab.remove(max(tab))
print(three)
