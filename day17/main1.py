import time


def is_clear(rock_shape, corner_cord, columns):
    for x, y in rock_shape:
        if 0 > (corner_cord[0] + x) or 6 < (corner_cord[0] + x):
            return False
        if (corner_cord[1] + y) in columns[(corner_cord[0] + x)]:
            return False
    return True


def add_to_columns(rock_shape, corner_cord, columns):
    for x, y in rock_shape:
        columns[corner_cord[0] + x].append(corner_cord[1] + y)


inputs = [-1 if shape == "<" else 1 for shape in open('data.txt', "r").read()]
inputs_len = len(inputs)
columns = [[0] for _ in range(0, 8)]
rock_shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # ----
    [(0, 1), (1, 0), (1, 1), (2, 1), (1, 2)],  # cross
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # L
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # |
    [(0, 0), (0, 1), (1, 0), (1, 1)]  # cube
]  # (x,y) offsets from bottom left corner of the shape. Base point might not be part of shape

start_time = time.time()
jet_counter = 0
for rock_nr in range(0, 2023):
    rock_shape = rock_shapes[rock_nr % 5]
    corner_cord = (2, max(max(heights) for heights in columns) + 4)

    while True:
        jet_offset = inputs[jet_counter % inputs_len]
        jet_counter += 1

        # jet
        if is_clear(rock_shape, (corner_cord[0] + jet_offset, corner_cord[1]), columns):
            corner_cord = (corner_cord[0] + jet_offset, corner_cord[1])

        # down
        if is_clear(rock_shape, (corner_cord[0], corner_cord[1] - 1), columns):
            corner_cord = (corner_cord[0], corner_cord[1] - 1)
        else:
            add_to_columns(rock_shape, corner_cord, columns)
            break

print("--- %s seconds ---" % (time.time() - start_time))
max_height = max(max(heights) for heights in columns)
print(max_height - 1 - 1)  # -1 for ground and -1 because I don't know
# # print out the resulting figure
# for i in range(max_height, -1, -1):
#     for x in range(7):
#         if i in columns[x]:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()
