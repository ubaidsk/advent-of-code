class Element:
    def __init__(self, val):
        self.val = val
        self.visited = False
    def __repr__(self):
        return f"{self.val}"

n = int(input())
arr = []
order_holder = {}
order_holder_rev = {}
for i in range(n):
    arr.append(Element(int(input()) * 811589153))
    order_holder[i] = i
    order_holder_rev[i] = i

def rotate(idx, val):
    global arr, n, order_holder

    val %= (n - 1)
    for i in range(val):
        cur_idx = (idx + i) % n
        next_idx = (idx + i + 1) % n

        order_no1 = order_holder_rev[cur_idx]
        order_no2 = order_holder_rev[next_idx]

        order_holder[order_no1] = next_idx
        order_holder[order_no2] = cur_idx

        order_holder_rev[next_idx] = order_no1
        order_holder_rev[cur_idx] = order_no2

        arr[cur_idx], arr[next_idx] = arr[next_idx], arr[cur_idx]
        # print(val, cur_idx, next_idx, arr)

def Mix():
    global arr, n, order_holder

    for i in arr:
        i.visited = False

    for i in range(n):
        idx = order_holder[i]
        arr[idx].visited = True
        val = arr[idx].val
        rotate(idx, val)

    for i in arr:
        if not i.visited:
            print(f"Not visited: {i.val}")

for _ in range(10):
    Mix()
    # print(arr)

zero_loc = None
for i, element in enumerate(arr):
    if element.val == 0:
        zero_loc = i

groove_coors = [zero_loc + 1000, zero_loc + 2000, zero_loc + 3000]
for i in range(3):
    groove_coors[i] %= n
    print(arr[groove_coors[i]])
print(sum(map(lambda i: arr[i].val, groove_coors)))
