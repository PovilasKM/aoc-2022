forest = [(list(x)) for x in open('data.txt', "r").read().split("\n")]
forest_visibility = [row[:] for row in forest]
length = len(forest)
for x in range(length):
    for y in range(length):
        cur = forest[x][y]
        forest_visibility[x][y] = 0
        if all(v[y] < cur for v in forest[:x]) \
            or all(v[y] < cur for v in forest[x + 1:]) \
            or all(v < cur for v in forest[x][:y]) \
            or all(v < cur for v in forest[x][y + 1:]):
            forest_visibility[x][y] = 1
print(sum(x for x in sum(forest_visibility, []) if x == 1))
