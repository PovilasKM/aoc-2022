import re


def try_point(point, coordinates):
    x, y = point
    covered = False
    for coord in coordinates:
        distance = abs(x - coord[0]) + abs(y - coord[1])
        if (coord[2], coord[3]) == (x, y):
            covered = True
            continue
        if (coord[0], coord[1]) == (x, y):
            covered = True
            continue
        if distance <= coord[4]:
            covered = True
            break
    if not covered:
        print(point)
        print((x * 4_000_000) + y)
        return True


lines = open('data.txt', "r").read().split("\n")
pattern = r'^Sensor at x=([-+]?[0-9]+), y=([-+]?[0-9]+): closest beacon is at x=([-+]?[0-9]+), y=([-+]?[0-9]+)$'
coordinates = []
for line in lines:
    g = re.search(pattern, line)
    reach = abs(int(g.group(1)) - int(g.group(3))) + abs(int(g.group(2)) - int(g.group(4)))
    coordinates.append((int(g.group(1)), int(g.group(2)), int(g.group(3)), int(g.group(4)), reach))

bound = 4_000_000  # 20 for example, 4_000_000 for input
for coord in coordinates:
    c_x, c_y, d = coord[0], coord[1], coord[4]
    #     corners:
    c1, c2, c3, c4 = (c_x, c_y + d + 1), (c_x + d + 1, c_y), (c_x, c_y - d - 1), (c_x - d - 1, c_y)
    for i in range(0, d + 2):
        #     c1->c2
        x, y = c1[0] + i, c1[1] - i
        if bound >= x >= 0 and bound >= y >= 0:
            if try_point((x, y), coordinates):
                break
        #     c2->c3
        x, y = c2[0] - i, c2[1] - i
        if bound >= x >= 0 and bound >= y >= 0:
            if try_point((x, y), coordinates):
                break
        #     c3->c4
        x, y = c3[0] - i, c3[1] + i
        if bound >= x >= 0 and bound >= y >= 0:
            if try_point((x, y), coordinates):
                break
        #     c4->c1
        x, y = c4[0] + i, c4[1] + i
        if bound >= x >= 0 and bound >= y >= 0:
            if try_point((x, y), coordinates):
                break
    else:
        continue
    break
