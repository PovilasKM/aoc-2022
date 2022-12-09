# ------------
# OBSOLETE: part 2 works for part 1 too.
# ------------
sign = lambda x: 1 if x >= 1 else -1 if x <= -1 else 0
directions = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}
f = open('data.txt', "r")
visited = set()
visited.add((0, 0))
h, t = (0, 0), (0, 0)
line = f.readline().strip()
while line:
    dir, dist = line.split()
    for _ in range(int(dist)):
        h = (h[0] + directions[dir][0], h[1] + directions[dir][1])
        xd, yd = h[0] - t[0], h[1] - t[1]
        if pow(xd, 2) + pow(yd, 2) > 2:
            t = (t[0] + sign(xd), t[1] + sign(yd))
            visited.add(t)
    line = f.readline().strip()
print("unique: ", len(visited))
