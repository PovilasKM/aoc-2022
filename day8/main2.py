from itertools import takewhile

forest = [(list(x)) for x in open('data.txt', "r").read().split("\n")]
length = len(forest)
forest_scores = [[0] * length for row in forest]
for x in range(1, length - 1):
    for y in range(1, length - 1):
        cur = forest[x][y]
        distances = [len(list(takewhile(lambda v: v[y] < cur, forest[x - 1::-1]))),
                     len(list(takewhile(lambda v: v[y] < cur, forest[x + 1:]))) + 1,
                     len(list(takewhile(lambda v: v < cur, forest[x][y - 1::-1]))),
                     len(list(takewhile(lambda v: v < cur, forest[x][y + 1:])))]
        score = 1
        for disc in distances:
            score *= disc
        forest_scores[x][y] = score
print(max(sum(forest_scores, [])))
