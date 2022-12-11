monkeys_inputs = open('data.txt', "r").read().split("\n\n")
monkey_items = [[] for _ in monkeys_inputs]
monkey_ops = []
monkey_tests = []
monkey_throw = [(-1, -1) for _ in monkeys_inputs]  # (if true, if false) throw id
for idx, monkey_input in enumerate(monkeys_inputs):
    lines = monkey_input.strip().split("\n")
    items = lines[1].split("items: ")[-1]
    monkey_items[idx] = [int(x) for x in items.split(", ")]
    monkey_ops.append(lines[2].split("new = ")[-1])  # use as eval(monkey_ops[x])
    monkey_tests.append(int(lines[3].split("divisible by ")[-1]))
    throw_to_true = int(lines[4].split("monkey ")[-1])
    throw_to_false = int(lines[5].split("monkey ")[-1])
    monkey_throw[idx] = (throw_to_true, throw_to_false)

inspects = [0 for x in monkeys_inputs]

rounds = 20
for _ in range(rounds):
    for monkey_idx, __ in enumerate(monkeys_inputs):
        for item_idx, item in enumerate(monkey_items[monkey_idx]):
            inspects[monkey_idx] += 1
            old = item
            new_worry = eval(monkey_ops[monkey_idx]) // 3
            is_divisible = 0 if new_worry % monkey_tests[monkey_idx] == 0 else 1
            monkey_items[monkey_throw[monkey_idx][is_divisible]].append(new_worry)
        monkey_items[monkey_idx] = []
sorted_inspects = sorted(inspects)
print(sorted_inspects[-1] * sorted_inspects[-2])
