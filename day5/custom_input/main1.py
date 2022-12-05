f = open('data.txt', "r")
number_of_columns = int(f.readline().strip())
crates = [[] for x in range(number_of_columns)]
line = f.readline().strip()
while line:
    for idx, letter in enumerate(line.split("|")):
        if letter:
            crates[idx].append(letter)
    line = f.readline().strip()

line = f.readline().strip()
while line:
    amount, from_crate_index, to_crate_index = [int(s) for s in line.split() if s.isdigit()]
    crates[to_crate_index - 1] = crates[from_crate_index - 1][amount - 1::-1] + crates[to_crate_index - 1]
    crates[from_crate_index - 1] = crates[from_crate_index - 1][amount:]
    line = f.readline().strip()

print("".join(x[0] for x in crates))
