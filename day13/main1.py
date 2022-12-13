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
indxs = []

for idx, pair in enumerate(pairs):
    left = json.loads(pair.split("\n")[0])
    right = json.loads(pair.split("\n")[1])
    if compare(left, right):
        indxs.append(idx + 1)

print(indxs)
print(sum(indxs))
