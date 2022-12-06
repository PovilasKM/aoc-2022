line = open('data.txt', "r").readline().strip()
print([i for i in range(13, len(line)) if len(set(line[i - 14:i])) == 14][0])
