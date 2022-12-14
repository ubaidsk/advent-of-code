input_insts = []

with open("input.txt") as inp:
    for line in inp.read().strip().split("\n"):
        dir_, steps = line.split(" ")
        steps = int(steps)
        input_insts.append([dir_, steps])

# puzzle 1
H, T = [0, 0], [0, 0]
unique_locs = set()
unique_locs.add(tuple(T))

dist = lambda h, t: max(abs(h[0] - t[0]), abs(h[1] - t[1]))

for inst in input_insts:
    dir_, steps = inst[0], inst[1]
    row_delta, col_delta = 0, 0
    if dir_ == "U":
        row_delta = -1
    elif dir_ == "D":
        row_delta = 1
    elif dir_ == "R":
        col_delta = 1
    else: # dir_ is "L"
        col_delta = -1

    for i in range(steps):
        prevR, prevC = H[0], H[1]
        H[0] = prevR + row_delta
        H[1] = prevC + col_delta
        if dist(H, T) > 1:
            T = [prevR, prevC]
        unique_locs.add(tuple(T))

print("puzzle1: %s" % len(unique_locs))


# puzzle 2
rope = [[0, 0] for _ in range(10)]
unique_locs = set()
unique_locs.add(tuple(rope[-1]))

for inst in input_insts:
    dir_, steps = inst[0], inst[1]
    row_delta, col_delta = 0, 0
    if dir_ == "U":
        row_delta = -1
    elif dir_ == "D":
        row_delta = 1
    elif dir_ == "R":
        col_delta = 1
    else: # dir_ is "L"
        col_delta = -1

    for _ in range(steps):
        prevR, prevC = rope[0][0], rope[0][1]
        rope[0][0] = prevR + row_delta
        rope[0][1] = prevC + col_delta
        for i in range(1, 10):
            if dist(rope[i - 1], rope[i]) > 1:
                nxt = rope[i - 1]
                neighs = [[nxt[0] + 1, nxt[1]], [nxt[0] - 1, nxt[1]], [nxt[0], nxt[1] + 1], [nxt[0], nxt[1] - 1]]
                nearest_neigh = neighs[0]
                nearest_dist = (nearest_neigh[0] - rope[i][0]) ** 2 + (nearest_neigh[1] - rope[i][1]) ** 2
                if abs(nxt[0] - rope[i][0]) + abs(nxt[1] - rope[i][1]) == 4:
                    neighs += [[nxt[0] + 1, nxt[1] + 1], [nxt[0] - 1, nxt[1] - 1], [nxt[0] - 1, nxt[1] + 1], [nxt[0] + 1, nxt[1] - 1]]
                for neigh in neighs[1:]:
                    neigh_dist = (neigh[0] - rope[i][0]) ** 2 + (neigh[1] - rope[i][1]) ** 2
                    if neigh_dist <= nearest_dist:
                        nearest_dist = neigh_dist
                        nearest_neigh = neigh
                rope[i] = nearest_neigh
        # print(rope)
        unique_locs.add(tuple(rope[-1]))

print("puzzle2: %s" % len(unique_locs))
