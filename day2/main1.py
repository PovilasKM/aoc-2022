response_scores = {"A Y": 2 + 6, "A X": 1 + 3, "A Z": 3, "B Y": 2 + 3, "B X": 1, "B Z": 3 + 6, "C Y": 2, "C X": 1 + 6,
                   "C Z": 3 + 3}
total = 0
for line in open('data.txt', "r"):
    total += response_scores[line.rstrip()]
print(total)
