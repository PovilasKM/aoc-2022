total = 0
for linen in open('data.txt', "r"):
    line = linen.rstrip("\n")
    first_group = line.split(",")[0].split("-")
    second_group = line.split(",")[1].split("-")
    first_area = set(range(int(first_group[0]), int(first_group[1])+1))
    second_area = set(range(int(second_group[0]), int(second_group[1])+1))
    if first_area.issubset(second_area) or second_area.issubset(first_area):
        total += 1
print(total)
