grid = ""
with open("input.txt") as inp:
    grid = [list(row) for row in inp.read().strip().split("\n")]

rows = len(grid)
cols = len(grid[0])

def get_char_loc(ch):
    global rows, cols, grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == ch:
                return (i, j)
    return (-1, -1)

src = get_char_loc("S")
des = get_char_loc("E")
grid[src[0]][src[1]] = "a"
grid[des[0]][des[1]] = "z"




# puzzle 1
def get_neighs(i, j):
    global grid, rows, cols
    neighs = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    possible_neighs = []
    for neigh in neighs:
        I, J = neigh
        if (I >= 0 and J >= 0 and I < rows and J < cols):
            if ord(grid[i][j]) - ord(grid[I][J]) >= -1:
                possible_neighs.append(neigh)
    return possible_neighs

from collections import deque

# Initializing a queue
q = deque()
q.append((src, 0))
visited = [[False for _ in range(cols)] for __ in range(rows)]
visited[src[0]][src[1]] = True

while q:
    front_element = q[0]
    q.popleft()
    cur = front_element[0]
    dist = front_element[1]
    if cur == des:
        print("puzzle1: %s" % dist)
        break

    for neigh in get_neighs(cur[0], cur[1]):
        I, J = neigh
        if not visited[I][J]:
            q.append((neigh, dist + 1))
            visited[I][J] = True

q.clear()
src = des
q.append((src, 0))
visited = [[False for _ in range(cols)] for __ in range(rows)]
visited[src[0]][src[1]] = True

def get_neighs2(i, j):
    global grid, rows, cols
    neighs = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    possible_neighs = []
    for neigh in neighs:
        I, J = neigh
        if (I >= 0 and J >= 0 and I < rows and J < cols):
            if ord(grid[i][j]) - ord(grid[I][J]) <= 1:
                possible_neighs.append(neigh)
    return possible_neighs

while q:
    front_element = q[0]
    q.popleft()
    cur = front_element[0]
    dist = front_element[1]
    if grid[cur[0]][cur[1]] == "a":
        print("puzzle2: %s" % dist)
        break

    for neigh in get_neighs2(cur[0], cur[1]):
        I, J = neigh
        if not visited[I][J]:
            q.append((neigh, dist + 1))
            visited[I][J] = True
