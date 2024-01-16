sanfi_num_sym = {
    0: "0",
    1: "1",
    2: "2",
    -1: "-",
    -2: "="
}

sanfi_sym_num = {
    "0": 0 ,
    "1": 1 ,
    "2": 2 ,
    "-": -1 ,
    "=": -2
}

def get_sanfi(n):
    global sanfi_num_sym

    a = []
    while(n):
        a.append(n % 5)
        n //= 5

    a.append(0)
    for i in range(len(a) - 1):
        if a[i] == 5:
            a[i] = 0
            a[i + 1] += 1
        elif a[i] == 4:
            a[i] = -1
            a[i + 1] += 1
        elif a[i] == 3:
            a[i] = -2
            a[i + 1] += 1

    return "".join(map(lambda x: sanfi_num_sym[x], a))[::-1]

def get_decimal(s):
    global sanfi_sym_num

    s = s[::-1]
    n = 0
    for i in range(len(s)):
        n += (5 ** i) * int(sanfi_sym_num[s[i]])
    return n

n = int(input())
total = 0
for i in range(n):
    num = get_decimal(input().strip())
    total += num

print("puzzle1: %s, %s" % (total, get_sanfi(total)))
