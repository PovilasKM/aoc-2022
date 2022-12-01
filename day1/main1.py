biggest = 0
temp = 0
for x in open('data.txt', "r"):
    line = x.rstrip("\n")
    if line:
        temp += int(line)
    else:
        if temp > biggest:
            biggest = temp
        temp = 0
print(biggest)
