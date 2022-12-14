stacks_raw = \
"""#H##D#P##
WB##CZD##
TJ#TJDJ##
HZ#HHWS#M
PFRPZFW#F
JVTNFGZSS
CRPSVMVDZ
FGHZNPMND"""

stacks_col_order = [list(i) for i in stacks_raw.split("\n")]
stacks = []

for j in range(len(stacks_col_order[0])):
    row = []
    for i in range(len(stacks_col_order) - 1, -1, -1):
        if stacks_col_order[i][j] == "#":
            break
        row.append(stacks_col_order[i][j])
    stacks.append(row)

print(stacks)

import re

pattern_cnt = r"(?<=move\s).+(?=\sfrom)"
pattern_src = r"(?<=from\s).+(?=\sto)"
pattern_des = r"(?<=to\s).+(?=\n)"


def move(cnt, src, des):
    crates_to_move = stacks[src - 1][-cnt:]
    stacks[src - 1] = stacks[src - 1][:-cnt]
    crates_to_move = crates_to_move[::-1]
    stacks[des - 1] += crates_to_move

with open("input.txt") as inp:
    for line in inp.readlines():
        cnt = re.search(pattern_cnt, line).group()
        src = re.search(pattern_src, line).group()
        des = re.search(pattern_des, line).group()
        move(int(cnt), int(src), int(des))

for row in stacks:
    print(row[-1], end="")
