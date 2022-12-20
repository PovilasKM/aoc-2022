total_sum = 0
lines = open('data.txt', "r").read().split("\n")
for i, line1 in [(i, x) for i, x in enumerate(lines)][::3]:
    line2, line3 = lines[i + 1], lines[i + 2]
    letter = (set(line1) & set(line2) & set(line3)).pop()
    total_sum += ord(letter) - 96 if letter.islower() else ord(letter) - 38

print(total_sum)
