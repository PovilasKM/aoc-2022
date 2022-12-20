biggest = 0
temp = 0
lines = open('data.txt', "r").read().split("\n")
for line in lines:
    if line:
        temp += int(line)
    else:
        if temp > biggest:
            biggest = temp
        temp = 0
print(biggest)
