def print_stuff(c, cx):
    cur_c = ((c-1) % 40)
    if cx in [cc for cc in range(cur_c - 1, cur_c + 2)]:
        print("#", end="")
    else:
        print(".", end="")
    if c % 40 == 0:
        print()


lines = open('data.txt', "r").read().split("\n")
x = 1
cycle = 0
for line in lines:
    if line == "noop":
        cycle += 1
        print_stuff(cycle, x)
    else:
        toadd = line.split()[1]
        cycle += 1
        print_stuff(cycle, x)
        cycle += 1
        print_stuff(cycle, x)
        x += int(toadd)
