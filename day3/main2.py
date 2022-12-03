total_sum = 0
f = open('data.txt', "r")
while True:
    line1, line2, line3 = f.readline(), f.readline(), f.readline()
    if not line1:
        break
    letter = (set(line1[:-1:]) & set(line2[:-1:]) & set(line3[:-1:])).pop()
    total_sum += ord(letter) - 96 if letter.islower() else ord(letter) - 38

print(total_sum)
