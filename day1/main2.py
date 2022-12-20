calories = []
temp = 0
lines = open('data.txt', "r").read().split("\n")
for line in lines:
    if line:
        temp += int(line)
    else:
        calories.append(temp)
        temp = 0
print(sum(sorted(calories, reverse=True)[0:3]))
