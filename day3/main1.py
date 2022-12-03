total_sum = 0
for line in open('data.txt', "r"):
    left, right = line[:len(line) // 2], line[len(line) // 2:]
    for letter in left:
        if letter in right:
            total_sum += ord(letter) - 96 if letter.islower() else ord(letter) - 38
            break

print(total_sum)
