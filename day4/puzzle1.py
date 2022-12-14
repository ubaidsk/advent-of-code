no_of_pairs = 0
with open("input.txt") as fd:
    for line in fd.readlines():
        elf1, elf2 = line.split(",")
        l0, r0 = map(int, elf1.split("-"))
        l1, r1 = map(int, elf2.split("-"))

        if (l1 <= l0 and r0 <= r1) or (l0 <= l1 and r1 <= r0):
            no_of_pairs += 1
    print(no_of_pairs)
