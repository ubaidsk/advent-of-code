no_of_pairs = 0
with open("input.txt") as fd:
    for line in fd.readlines():
        elf1, elf2 = line.split(",")
        l0, r0 = map(int, elf1.split("-"))
        l1, r1 = map(int, elf2.split("-"))
        ranges = [[l0, r0], [l1, r1]]
        ranges.sort(key=lambda x: x[0])

        if (ranges[1][0] <= ranges[0][1]):
            no_of_pairs += 1

    print(no_of_pairs)
