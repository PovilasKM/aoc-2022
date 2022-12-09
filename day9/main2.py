sign = lambda x: 1 if x >= 1 else -1 if x <= -1 else 0
directions = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}
f = open('data.txt', "r")
visited = set()
visited.add((0, 0))
hcord, tcords = (0, 0), [(0, 0) for x in range(9)]
line = f.readline().strip()
while line:
    dir, dist = line.split()
    for _ in range(int(dist)):
        hcord = (hcord[0] + directions[dir][0], hcord[1] + directions[dir][1])
        cur_h = hcord
        for idx, cur_t in enumerate(tcords):
            xd, yd = cur_h[0] - cur_t[0], cur_h[1] - cur_t[1]
            if pow(xd, 2) + pow(yd, 2) <= 2:
                cur_h = cur_t
                continue  # don't move t
            tcords[idx] = (cur_t[0] + sign(xd), cur_t[1] + sign(yd))
            cur_h = tcords[idx]
        visited.add(tcords[-1])
    line = f.readline().strip()
print("unique: ", len(visited))
