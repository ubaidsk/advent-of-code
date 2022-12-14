paths = []
with open("input.txt") as inp:
    for line in inp.read().strip().split("\n"):
        locs = []
        for loc in line.split(" -> "):
            locs.append(list(map(int, loc.split(","))))
        paths.append(locs)

xmax = -1
ymax = -1
xmin, ymin = 100000, 10000
print(len(paths))
for path in paths:
    print(len(path))
    for loc in path:
        xmax = max(xmax, loc[0])
        ymax = max(ymax, loc[1])

        xmin = min(xmin, loc[0])
        ymin = min(ymin, loc[1])
        print(loc[0], loc[1])
# print(xmax, ymax)
# print(xmin, ymin)
