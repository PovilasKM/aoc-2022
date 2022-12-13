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
indxs = []

for idx, pair in enumerate(pairs):
    left = json.loads(pair.split("\n")[0])
    right = json.loads(pair.split("\n")[1])
    if compare_left_right(left, right):
        indxs.append(idx + 1)

print(indxs)
print(sum(indxs))
