class MFile:
    size = 0
    name = ""

    def __init__(self, size, name):
        self.size = size
        self.name = name


class Directory:
    path = ""
    directories = []
    files = []
    size = 0

    def __init__(self, path):
        self.path = path
        self.directories = []
        self.files = []
        self.size = 0


def get_directory(top_dir, path):
    if top_dir.path == path:
        return top_dir
    for directory in top_dir.directories:
        temp = get_directory(directory, path)
        if temp:
            return temp
    return None


def calculate_sizes(top_dir):
    total = 0
    for file in top_dir.files:
        total += file.size
    for directory in top_dir.directories:
        total += calculate_sizes(directory)
    top_dir.size = total
    return total


def get_answer_size(top_dir):
    total = 0
    if top_dir.size <= 100000:
        total += top_dir.size
    for directory in top_dir.directories:
        total += get_answer_size(directory)
    return total


f = open('data.txt', "r")
current_path = ""
top_dir = Directory("/")
line = f.readline().strip()
while line:
    if line[0] == "$":
        if line[2:4] == "ls":
            line = f.readline().strip()
            continue  # noop?
        else:  # cd
            rel_path = line.split(" ")[2]
            if rel_path == "/":
                current_path = rel_path
            elif rel_path == "..":
                last_index = current_path.rfind("/")
                current_path = current_path[:last_index]
            else:  # cd some_path
                if current_path == "/":
                    current_path += rel_path
                else:
                    current_path += "/" + rel_path

    elif line[:4] == "dir ":
        dir_name = line.split(" ")[1]
        if not get_directory(top_dir, current_path + "/" + dir_name):
            cur_dir = get_directory(top_dir, current_path)
            new_dir = Directory((current_path if current_path == "/" else current_path + "/") + dir_name)
            cur_dir.directories.append(new_dir)
    else:  # das a file
        size, name = line.split(" ")
        cur_dir = get_directory(top_dir, current_path)
        cur_dir.files.append(MFile(int(size), name))

    line = f.readline().strip()

calculate_sizes(top_dir)
print(get_answer_size(top_dir))
