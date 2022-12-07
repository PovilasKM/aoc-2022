f = open('data.txt', "r")
current_path = [""]
dirs = {"": 0}
f.readline()  # ignore first line
line = f.readline().strip()
while line:
    if line[:4] == "$ cd":
        rel_path = line.split(" ")[2]
        if rel_path == "..":
            current_path.pop()
        else:
            current_path.append(rel_path)
    elif line[:4] == "dir ":
        dirs["/".join(current_path + [line.split(" ")[1]])] = 0
    elif line[0] != "$":  # das a file
        for i in range(len(current_path)):
            dirs["/".join(current_path[:i + 1])] += int(line.split(" ")[0])

    line = f.readline().strip()

unused_space = 70000000 - dirs[""]
required_space = 30000000 - unused_space
print(min(value for (key, value) in dirs.items() if value > required_space))
