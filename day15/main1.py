import re

lines = open('data.txt', "r").read().split("\n")
pattern = r'^Sensor at x=([-+]?[0-9]+), y=([-+]?[0-9]+): closest beacon is at x=([-+]?[0-9]+), y=([-+]?[0-9]+)$'
coordinates = []
for line in lines:
    g = re.search(pattern, line)
    reach = abs(int(g.group(1)) - int(g.group(3))) + abs(int(g.group(2)) - int(g.group(4)))
    coordinates.append((int(g.group(1)), int(g.group(2)), int(g.group(3)), int(g.group(4)), reach))
max_x_b = max(coord[2] for coord in coordinates)
max_x_a = max(coord[0] + coord[4] for coord in coordinates)
max_x = max(max_x_a, max_x_a)
min_x_b = min(coord[2] for coord in coordinates)
min_x_a = min(coord[0] - coord[4] for coord in coordinates)
min_x = min(min_x_a, min_x_b)

y = 2000000  # 10 for example, 2000000 for input
covered_count = 0
for x in range(min_x, max_x + 1):
    covered = False
    for coord in coordinates:
        distance = abs(x - coord[0]) + abs(y - coord[1])
        if (coord[2], coord[3]) == (x, y):
            continue
        if (coord[0], coord[1]) == (x, y):
            continue
        if distance <= coord[4]:
            covered = True
            break
    if covered:
        covered_count += 1
print(covered_count)
