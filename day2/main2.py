response_scores = {"AY": 1 + 3, "AX": 3 + 0, "AZ": 2 + 6, "BY": 2 + 3, "BX": 1 + 0, "BZ": 3 + 6, "CY": 3 + 3,
                   "CX": 2 + 0, "CZ": 1 + 6}
total = 0
for line in open('data.txt', "r"):
    total += response_scores[line[0] + line[2]]
print(total)
