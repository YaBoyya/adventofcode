sum = 0

with open("2023/input/1.txt", "r") as f:
    for line in f.readlines():
        nums = list(filter(str.isdigit, line))
        val = int(nums[0]+nums[-1])
        sum += val

print(sum)
