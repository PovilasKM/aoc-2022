import json


def compare(left, right):
    if type(left) == type(right) == list:
        res = None
        if len(left) < len(right):
            res = True
        if len(left) > len(right):
            res = False
        for el_left, el_right in zip(left, right):
            temp_res = compare(el_left, el_right)
            if temp_res is None:
                continue
            else:
                return temp_res
        return res
    elif type(left) == type(right) == int:
        if left > right:
            return False
        if left < right:
            return True
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])


pairs = open('data.txt', "r").read().split("\n\n")
lines = [json.loads(item) for pair in pairs for item in pair.split("\n")]
dividers = [[[2]], [[6]]]
lines.extend(dividers)

n = len(lines)
swapped = False
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if not compare(lines[j], lines[j+1]):
            swapped = True
            lines[j], lines[j + 1] = lines[j + 1], lines[j]

a = lines.index(dividers[0]) + 1
b = lines.index(dividers[1]) + 1
print(a, b, a*b)
