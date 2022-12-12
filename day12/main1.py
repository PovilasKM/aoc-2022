rows = open('data.txt', "r").read().split("\n")
length = len(rows[0])
height = len(rows)
ground_x = lambda x: 0 if x < 0 else x if x < height else height - 1
ground_y = lambda x: 0 if x < 0 else x if x < length else length - 1
distances = [[-1 for y in range(length + 2)] if (x == 0 or x == height + 1) else [-1 if (y == 0 or y == length + 1) else 999 for y in range(length + 2)] for x in range(height + 2)]
rows_int = [[0 for _ in range(length)] for _ in range(height)]
start, end = (0, 0), (0, 0)
for row_number, row in enumerate(rows):
    for row_idx, x in enumerate(row):
        if x == "S":
            start = (row_number + 1, row_idx + 1)
            distances[start[0]][start[1]] = 0
            rows[row_number] = rows[row_number][:row_idx] + "a" + rows[row_number][row_idx + 1:]
        if x == "E":
            end = (row_number + 1, row_idx + 1)
            rows[row_number] = rows[row_number][:row_idx] + "z" + rows[row_number][row_idx + 1:]
        rows_int[row_number][row_idx] = ord(x)

for_check = set()
for_check.add(start)
while len(for_check):
    to_add = set()
    for check in for_check:
        x, y = check
        f_ord = ord(rows[x - 1][y - 1])
        d = distances[x][y]
        if distances[x + 1][y] != -1 and \
            distances[x + 1][y] > d + 1 and f_ord - ord(rows[ground_x(x + 1 - 1)][ground_y(y - 1)]) >= -1:
            distances[x + 1][y] = d + 1
            to_add.add((x + 1, y))
        if distances[x][y + 1] != -1 and \
            distances[x][y + 1] > d + 1 and f_ord - ord(rows[ground_x(x - 1)][ground_y(y + 1 - 1)]) >= -1:
            distances[x][y + 1] = d + 1
            to_add.add((x, y + 1))
        if distances[x - 1][y] != -1 and \
            distances[x - 1][y] > d + 1 and f_ord - ord(rows[ground_x(x - 1 - 1)][ground_y(y - 1)]) >= -1:
            distances[x - 1][y] = d + 1
            to_add.add((x - 1, y))
        if distances[x][y - 1] != -1 and \
            distances[x][y - 1] > d + 1 and f_ord - ord(rows[ground_x(x - 1)][ground_y(y - 1 - 1)]) >= -1:
            distances[x][y - 1] = d + 1
            to_add.add((x, y - 1))
    for_check = to_add
print(distances[end[0]][end[1]])
