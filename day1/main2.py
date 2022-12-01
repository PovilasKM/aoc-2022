calories = []
temp = 0
for x in open('data.txt', "r"):
    line = x.rstrip("\n")
    if line:
        temp += int(line)
    else:
        calories.append(temp)
        temp = 0
calories.sort(reverse=True)
print(sum(calories[0:3]))
