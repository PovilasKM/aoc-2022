line = open('data.txt', "r").readline().strip()
print([i for i in range(3, len(line)) if len(set(line[i - 4:i])) == 4][0])
