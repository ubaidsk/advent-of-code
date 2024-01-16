class Element:
    def __init__(self, val):
        self.val = val
        self.visited = False
    def __repr__(self):
        return f"{self.val}"

n = int(input())
arr = []
for i in range(n):
    arr.append(Element(int(input())))

def rotate(idx, val):
    global arr

    val %= (n - 1)
    for i in range(val):
        cur_idx = (idx + i) % n
        next_idx = (idx + i + 1) % n
        arr[cur_idx], arr[next_idx] = arr[next_idx], arr[cur_idx]
        # print(val, cur_idx, next_idx, arr)

idx = 0
while idx < n:
    if arr[idx].visited:
        idx += 1
        continue
    # print("=" * 25)
    # print(arr)
    arr[idx].visited = True
    val = arr[idx].val
    rotate(idx, val)
    if idx < 0: idx = 0

for i in arr:
    if not i.visited:
        print(f"Not visited: {i.val}")

zero_loc = None
for i, element in enumerate(arr):
    if element.val == 0:
        zero_loc = i

groove_coors = [zero_loc + 1000, zero_loc + 2000, zero_loc + 3000]
for i in range(3):
    groove_coors[i] %= n
    print(arr[groove_coors[i]])
print(sum(map(lambda i: arr[i % n].val, groove_coors)))
