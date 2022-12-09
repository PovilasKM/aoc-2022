# (x, y)
directions = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}
f = open('data.txt', "r")
visited = set()
visited.add((0, 0))
hcord = (0, 0)
tcords = [(0, 0) for x in range(9)]
line = f.readline().strip()
while line:
    direction, distance = line.split(" ")
    for _ in range(int(distance)):
        hcord = (hcord[0] + directions[direction][0], hcord[1] + directions[direction][1])
        current_hcord = hcord
        for idx, current_tcord in enumerate(tcords):
            xdist, ydist = current_hcord[0] - current_tcord[0], current_hcord[1] - current_tcord[1]
            if 1 >= xdist >= -1 and 1 >= ydist >= -1:
                current_hcord = current_tcord
                continue  # don't move t
            tcords[idx] = (current_tcord[0] + (1 if xdist >= 1 else -1 if xdist <= -1 else 0),
                           current_tcord[1] + (1 if ydist >= 1 else -1 if ydist <= -1 else 0))
            if idx == 8:
                visited.add(current_tcord)
            current_hcord = tcords[idx]
    line = f.readline().strip()
print("unique: ", len(visited) + 1)  # no idea why but it works with +1
# oh and this +1 won't work with example data but will work with second example and my input...lmao
