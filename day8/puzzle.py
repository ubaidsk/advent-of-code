grid = []
with open("input.txt") as inp:
    for row in inp.read().split("\n"):
        if row:
            grid.append(list(map(int, row)))

visible_trees = set()

rows = len(grid)
cols = len(grid[0])

# puzzle 1
for j in range(cols):
    mx = -1
    for i in range(rows):
        if grid[i][j] > mx:
            visible_trees.add((i, j))
            mx = grid[i][j]

for j in range(cols):
    mx = -1
    for i in range(rows - 1, -1, -1):
        if grid[i][j] > mx:
            visible_trees.add((i, j))
            mx = grid[i][j]

for i in range(rows):
    mx = -1
    for j in range(cols):
        if grid[i][j] > mx:
            visible_trees.add((i, j))
            mx = grid[i][j]


for i in range(rows):
    mx = -1
    for j in range(cols - 1, -1, -1):
        if grid[i][j] > mx:
            visible_trees.add((i, j))
            mx = grid[i][j]

print("puzzle1: %s" % len(visible_trees))

# puzzle2

viewing_dists = [[[] for j in range(cols)] for i in range(rows)]

for j in range(cols):
    stack = []
    for i in range(rows):
        while stack and stack[-1][2] <= grid[i][j]:
            I, J, H = stack[-1]
            viewing_dists[I][J].append(i - I)
            stack.pop()
        stack.append([i, j, grid[i][j]])
    while stack:
        I, J, H = stack[-1]
        viewing_dists[I][J].append(rows - 1 - I)
        stack.pop()

for j in range(cols):
    stack = []
    for i in range(rows - 1, -1, -1):
        while stack and stack[-1][2] <= grid[i][j]:
            I, J, H = stack[-1]
            viewing_dists[I][J].append(i - I)
            stack.pop()
        stack.append([i, j, grid[i][j]])
    while stack:
        I, J, H = stack[-1]
        viewing_dists[I][J].append(0 - I)
        stack.pop()

for i in range(rows):
    stack = []
    for j in range(cols):
        while stack and stack[-1][2] <= grid[i][j]:
            I, J, H = stack[-1]
            viewing_dists[I][J].append(j - J)
            stack.pop()
        stack.append([i, j, grid[i][j]])
    while stack:
        I, J, H = stack[-1]
        viewing_dists[I][J].append(cols - 1 - J)
        stack.pop()


for i in range(rows):
    stack = []
    for j in range(cols - 1, -1, -1):
        while stack and stack[-1][2] <= grid[i][j]:
            I, J, H = stack[-1]
            viewing_dists[I][J].append(j - J)
            stack.pop()
        stack.append([i, j, grid[i][j]])
    while stack:
        I, J, H = stack[-1]
        viewing_dists[I][J].append(0 - J)
        stack.pop()

ans = 0
for i in range(rows):
    for j in range(cols):
        l, r, t, b = viewing_dists[i][j]
        scenic_score = l * r * t * b
        ans = max(ans, abs(scenic_score))

print("puzzle2: %s" % ans)
