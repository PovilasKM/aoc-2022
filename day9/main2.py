sign = lambda x: 1 if x >= 1 else -1 if x <= -1 else 0
directions = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}
lines = open('data.txt', "r").read().split("\n")
visited = set()
rope = [(0, 0)] * 10  # change 10 to 2 for PART 1
for line in lines:
    dir, dist = line.split()
    for _ in range(int(dist)):
        rope[0] = (rope[0][0] + directions[dir][0], rope[0][1] + directions[dir][1])
        for idx, knot in enumerate(rope[1:]):
            xd, yd = rope[idx][0] - knot[0], rope[idx][1] - knot[1]
            if pow(xd, 2) + pow(yd, 2) > 2:
                rope[idx + 1] = (knot[0] + sign(xd), knot[1] + sign(yd))
        visited.add(rope[-1])
print("unique: ", len(visited))
