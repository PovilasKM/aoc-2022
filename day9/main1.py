# (x, y)
directions = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}
f = open('data.txt', "r")
visited = set()
visited.add((0, 0))
hcord = (0, 0)
tcord = (0, 0)
line = f.readline().strip()
while line:
    direction, distance = line.split(" ")
    for _ in range(int(distance)):
        hcord = (hcord[0] + directions[direction][0], hcord[1] + directions[direction][1])
        xdist, ydist = hcord[0] - tcord[0], hcord[1] - tcord[1]
        if 1 >= xdist >= -1 and 1 >= ydist >= -1:
            continue  # don't move t
        tcord = (tcord[0] + (1 if xdist >= 1 else -1 if xdist <= -1 else 0),
                 tcord[1] + (1 if ydist >= 1 else -1 if ydist <= -1 else 0))
        visited.add(tcord)
    line = f.readline().strip()
print("unique: ", len(visited))
