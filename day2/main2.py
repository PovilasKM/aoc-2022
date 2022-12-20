response_scores = {"A Y": 1 + 3, "A X": 3 + 0, "A Z": 2 + 6, "B Y": 2 + 3, "B X": 1 + 0, "B Z": 3 + 6, "C Y": 3 + 3,
                   "C X": 2 + 0, "C Z": 1 + 6}
total = 0
for line in open('data.txt', "r"):
    total += response_scores[line.rstrip()]
print(total)
