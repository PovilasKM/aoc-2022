def add_cycle(c, cx, strs):
    if (c - 20) % 40 == 0:
        print(c, cx)
        strs.append(c * cx)


lines = open('data.txt', "r").read().split("\n")
x = 1
cycle = 0
str = []
for line in lines:
    if line == "noop":
        cycle += 1
        add_cycle(cycle, x, str)
    else:
        toadd = line.split()[1]
        cycle += 1
        add_cycle(cycle, x, str)
        cycle += 1
        add_cycle(cycle, x, str)
        x += int(toadd)
print(str)
print(sum(str))
