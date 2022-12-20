total = 0
lines = open('data.txt', "r").read().split("\n")
for line in lines:
    first_group = line.split(",")[0].split("-")
    second_group = line.split(",")[1].split("-")
    first_area = set(range(int(first_group[0]), int(first_group[1]) + 1))
    second_area = set(range(int(second_group[0]), int(second_group[1]) + 1))
    if len(first_area & second_area):
        total += 1
print(total)
