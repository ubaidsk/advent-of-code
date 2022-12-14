insts = []
with open("input.txt") as inp:
    for line in inp.read().strip().split("\n"):
        if line == "noop":
            insts.append([line, 0])
        else:
            inst, num = line.split(" ")
            insts.append(["noop", 0])
            insts.append([inst, int(num)])


# puzzle 1
cycles_for_sig_strength = [20]
for _ in range(5):
    cycles_for_sig_strength.append(cycles_for_sig_strength[-1] + 40)

low = 0
no_of_cycles = 1
reg_val = 1
sum_of_signal_strengths = 0
for inst in insts:
    if low < len(cycles_for_sig_strength) and no_of_cycles == cycles_for_sig_strength[low]:
        signal_strength = cycles_for_sig_strength[low] * reg_val
        low += 1
        sum_of_signal_strengths += signal_strength

    reg_val += inst[1]
    no_of_cycles += 1

print("puzzle1: %s" % sum_of_signal_strengths)

# puzzle 2
reg_val = 1
rows = 6
cols = 40
no_of_cycles = 1

for row in range(rows):
    for col in range(cols):
        if col >= reg_val - 1 and col <= reg_val + 1:
            print("#", end = "")
        else:
            print(".", end = "")
        reg_val += insts[no_of_cycles - 1][1]
        no_of_cycles += 1

    print()
