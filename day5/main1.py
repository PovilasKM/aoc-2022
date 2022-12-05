crates_input = []
f = open('data.txt', "r")
while True:
    line = f.readline()
    if not line.strip():
        break
    crates_input.append(line[:-1])

number_of_columns = len([x for x in crates_input[-1].split(" ") if x])
crates = [[] for x in range(number_of_columns)]

for i in range(1, number_of_columns*4, 4):
    for crate in crates_input[:-1]:
        if crate[i].strip():
            crates[(i//4)].append(crate[i])

while True:
    line = f.readline().strip()
    if not line:
        break
    amount, from_crate_index, to_crate_index = [int(s) for s in line.split() if s.isdigit()]
    from_crate_index -= 1
    to_crate_index -= 1
    to_move = crates[from_crate_index][:amount]
    to_move.reverse()
    crates[to_crate_index] = to_move + crates[to_crate_index]
    crates[from_crate_index] = crates[from_crate_index][amount:]

print("".join([x[0] for x in crates]))
