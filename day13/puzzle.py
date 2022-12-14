import json

def string_to_array(s):
  return json.loads(s)


packet_pairs = []
with open("input.txt") as inp:
    for pair_line in inp.read().strip().split("\n\n"):
        pair = pair_line.split("\n")
        left = string_to_array(pair[0])
        right = string_to_array(pair[1])
        packet_pairs.append([left, right])

def compare_list(l1, l2):
    n1 = len(l1)
    n2 = len(l2)
    for i in range(min(n1, n2)):
        cmp = compare(l1[i], l2[i])
        if cmp == -1:
            return -1
        elif cmp == 0:
            continue
        else:
            return 1
    if n1 < n2:
        return -1
    elif n1 == n2:
        return 0
    else:
        return 1


def compare(e1, e2):
    if (type(e1) is int) and (type(e2) is int):
        if e1 < e2:
            return -1
        elif e1 == e2:
            return 0
        else:
            return 1
    elif type(e1) is int:
        e1 = [e1]
    elif type(e2) is int:
        e2 = [e2]
    return compare_list(e1, e2)

correct_pairs_cnt = 0
for idx, pair in enumerate(packet_pairs):
    cmp = compare(pair[0], pair[1])
    if cmp == -1:
        correct_pairs_cnt += idx + 1

print(correct_pairs_cnt)

packets = []
for pair in packet_pairs:
    packets += pair
packets += [[[2]], [[6]]]

from functools import cmp_to_key
packets.sort(key=cmp_to_key(compare))

idx1 = -1
idx2 = -1
for idx, packet in enumerate(packets):
    if packet == [[2]]:
        idx1 = idx + 1
    elif packet == [[6]]:
        idx2 = idx + 1

print(idx1 * idx2)
