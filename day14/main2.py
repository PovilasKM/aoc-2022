lines = open('data.txt', "r").read().split("\n")
points_str = [line.split("->") for line in lines]
points = [[(int(item.strip().split(",")[0]), int(item.strip().split(",")[1])) for item in line] for line in points_str]
xs = [point[0] for line in points for point in line]
max_y = max([point[1] for line in points for point in line]) + 2
max_width = (max_y * 2) + 1
min_x, max_x = 500 - max_y, 500 + max_y
columns = [[max_y] for _ in range(max_width)]
print(min_x, max_x, max_y)

# prefill rocks
for line in points:
    for point_idx, (x, y) in enumerate(line[:-1]):
        (nx, ny) = line[point_idx + 1]  # next point
        if x == nx:  # movement is in y
            for i in range(min(y, ny), max(y, ny) + 1):
                columns[nx - min_x].append(i)
        else:  # movement is in x
            for i in range(min(x, nx), max(x, nx) + 1):
                columns[i - min_x].append(y)

sand = 0
while True:
    sand_p = (500 - min_x, 0)
    for y in range(1, max_y + 1):
        if not (y in columns[sand_p[0]]):  # down
            sand_p = (sand_p[0], y)
        elif not (y in columns[sand_p[0] - 1]):  # left
            sand_p = (sand_p[0] - 1, y)
        elif not (y in columns[sand_p[0] + 1]):  # right
            sand_p = (sand_p[0] + 1, y)
        else:  # no space
            if not (sand_p[1] in columns[sand_p[0]]):  # add sand
                columns[sand_p[0]].append(sand_p[1])
            break
    sand += 1
    if sand_p == (500 - min_x, 0):
        break

print(sand)
