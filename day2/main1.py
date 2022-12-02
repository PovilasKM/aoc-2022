response_scores = {"AY": 2 + 6, "AX": 1 + 3, "AZ": 3, "BY": 2 + 3, "BX": 1, "BZ": 3 + 6, "CY": 2, "CX": 1 + 6,
                   "CZ": 3 + 3}
total = 0
for line in open('data.txt', "r"):
    total += response_scores[line[0] + line[2]]
print(total)
