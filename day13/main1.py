import json


def compare_left_right(left, right):
    if type(left) == type(right) == list:
        res = None
        if len(left) < len(right):
            res = True
        if len(left) > len(right):
            res = False
        for el_left, el_right in zip(left, right):
            temp_res = compare_left_right(el_left, el_right)
            if temp_res is None:
                continue
            else:
                return temp_res
        return res
    if type(left) == type(right) == int:
        if left > right:
            return False
        if left < right:
            return True
    if isinstance(left, int) and isinstance(right, list):
        return compare_left_right([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return compare_left_right(left, [right])


pairs = open('data.txt', "r").read().split("\n\n")
lines = [json.loads(item) for pair in pairs for item in pair.split("\n")]

n = len(lines)
swapped = False
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if not compare_left_right(lines[j], lines[j+1]):
            swapped = True
            lines[j], lines[j + 1] = lines[j + 1], lines[j]

a = lines.index([[2]]) + 1
b = lines.index([[6]]) + 1
print(a, b, a*b)
