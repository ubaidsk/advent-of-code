import sys

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.area = [["." for _ in range(cols)] for __ in range(rows)]
        self.left_max = 0
        self.right_max = cols - 1
        self.down_max = rows - 1
        self.highest_level = rows - 4
    def place(self, block):
        for point in block.points:
            self.area[point[1]][point[0]] = "#"
        highest_point = block.get_highest_point()
        self.highest_level = min(self.highest_level, highest_point[1] - 4)
    def can_move_down(self, block):
        for point in block.points:
            if point[1] == self.down_max or self.area[point[1] + 1][point[0]] == "#":
                return False
        return True
    def can_move_left(self, block):
        for point in block.points:
            if point[0] == self.left_max or self.area[point[1]][point[0] - 1] == "#":
                return False
        return True
    def can_move_right(self, block):
        for point in block.points:
            if (point[0] == self.right_max) or (grid.area[point[1]][point[0] + 1] == "#"):
                return False
        return True

class Block:
    def __init__(self, points):
        self.points = []
        for point in points:
            self.points.append(point[:])
        points.sort(key = lambda x: x[1])
        self.height = points[-1][1] - points[0][1] + 1
    def move_left(self):
        self.points = list(map(lambda x: [x[0] - 1, x[1]], self.points))
    def move_down(self):
        self.points = list(map(lambda x: [x[0], x[1] + 1], self.points))
    def move_right(self):
        self.points = list(map(lambda x: [x[0] + 1, x[1]], self.points))
    def get_highest_point(self):
        return sorted(self.points, key=lambda x: x[1])[0]
    def update_with_offset(self, x_offset, y_offset):
        for point in self.points:
            point[0] += x_offset
            point[1] += y_offset

minus = [[0, 0], [1, 0], [2, 0], [3, 0]]
plus = [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]]
lmirr = [[2, 0], [2, 1], [2, 2], [1, 2], [0, 2]]
line = [[0, 0], [0, 1], [0, 2], [0, 3]]
box = [[0, 0], [0, 1], [1, 0], [1, 1]]

block_list = [minus, plus, lmirr, line, box]
grid = Grid(10000, 7)

stream = ""
stream_idx = 0
with open(sys.argv[1]) as inp:
    stream = inp.read().strip()

for i in range(2022):
    block_points = block_list[i % len(block_list)]
    block = Block(block_points)
    block.update_with_offset(2, grid.highest_level - (block.height - 1))
    while True:
        direct = stream[stream_idx % len(stream)]
        stream_idx += 1

        if direct == ">":
            if grid.can_move_right(block):
                block.move_right()
        elif direct == "<":
            if grid.can_move_left(block):
                block.move_left()
        else:
            print("Incorrect direction")

        if grid.can_move_down(block):
            block.move_down()
        else:
            grid.place(block)
            break
print("puzzle1: %s" % (grid.rows - grid.highest_level - 4))

def print_grid(start_row, end_row):
    for i in range(start_row, end_row + 1):
        print(f'|{"".join(grid.area[i])}|')
    print("+-------+")

for i in range(grid.rows):
    if "".join(grid.area[i]) == "#######":
        print(i, end=" ")
print()

print_grid(6981, 7111)
