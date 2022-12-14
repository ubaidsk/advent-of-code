Monkey0Items = [97, 81, 57, 57, 91, 61]
Monkey0ItemsInspectedCnt = 0
Monkey1Items = [88, 62, 68, 90]
Monkey1ItemsInspectedCnt = 0
Monkey2Items = [74, 87]
Monkey2ItemsInspectedCnt = 0
Monkey3Items = [53, 81, 60, 87, 90, 99, 75]
Monkey3ItemsInspectedCnt = 0
Monkey4Items = [57]
Monkey4ItemsInspectedCnt = 0
Monkey5Items = [54, 84, 91, 55, 59, 72, 75, 70]
Monkey5ItemsInspectedCnt = 0
Monkey6Items = [95, 79, 79, 68, 78]
Monkey6ItemsInspectedCnt = 0
Monkey7Items = [61, 97, 67]
Monkey7ItemsInspectedCnt = 0

MOD  = 11 * 19 * 5 * 2 * 13 * 7 * 3 * 17

def Monkey0():
    global Monkey0Items, Monkey0ItemsInspectedCnt
    for item in Monkey0Items:
        item %= MOD
        item = item * 7
        if (item % 11 == 0):
            Monkey5Items.append(item)
        else:
            Monkey6Items.append(item)
    Monkey0ItemsInspectedCnt += len(Monkey0Items)
    Monkey0Items = []

def Monkey1():
    global Monkey1Items, Monkey1ItemsInspectedCnt
    for item in Monkey1Items:
        item %= MOD
        item = item * 17
        if (item % 19 == 0):
            Monkey4Items.append(item)
        else:
            Monkey2Items.append(item)
    Monkey1ItemsInspectedCnt += len(Monkey1Items)
    Monkey1Items = []

def Monkey2():
    global Monkey2Items, Monkey2ItemsInspectedCnt
    for item in Monkey2Items:
        item %= MOD
        item = item + 2
        if (item % 5 == 0):
            Monkey7Items.append(item)
        else:
            Monkey4Items.append(item)
    Monkey2ItemsInspectedCnt += len(Monkey2Items)
    Monkey2Items = []

def Monkey3():
    global Monkey3Items, Monkey3ItemsInspectedCnt
    for item in Monkey3Items:
        item %= MOD
        item = item + 1
        if (item % 2 == 0):
            Monkey2Items.append(item)
        else:
            Monkey1Items.append(item)
    Monkey3ItemsInspectedCnt += len(Monkey3Items)
    Monkey3Items = []

def Monkey4():
    global Monkey4Items, Monkey4ItemsInspectedCnt
    for item in Monkey4Items:
        item %= MOD
        item = item + 6
        if (item % 13 == 0):
            Monkey7Items.append(item)
        else:
            Monkey0Items.append(item)
    Monkey4ItemsInspectedCnt += len(Monkey4Items)
    Monkey4Items = []

def Monkey5():
    global Monkey5Items, Monkey5ItemsInspectedCnt
    for item in Monkey5Items:
        item %= MOD
        item = item * item
        if (item % 7 == 0):
            Monkey6Items.append(item)
        else:
            Monkey3Items.append(item)
    Monkey5ItemsInspectedCnt += len(Monkey5Items)
    Monkey5Items = []

def Monkey6():
    global Monkey6Items, Monkey6ItemsInspectedCnt
    for item in Monkey6Items:
        item %= MOD
        item = item + 3
        if (item % 3 == 0):
            Monkey1Items.append(item)
        else:
            Monkey3Items.append(item)
    Monkey6ItemsInspectedCnt += len(Monkey6Items)
    Monkey6Items = []

def Monkey7():
    global Monkey7Items, Monkey7ItemsInspectedCnt
    for item in Monkey7Items:
        item %= MOD
        item = item + 4
        if (item % 17 == 0):
            Monkey0Items.append(item)
        else:
            Monkey5Items.append(item)
    Monkey7ItemsInspectedCnt += len(Monkey7Items)
    Monkey7Items = []

for _ in range(10000):
    Monkey0()
    Monkey1()
    Monkey2()
    Monkey3()
    Monkey4()
    Monkey5()
    Monkey6()
    Monkey7()

InspectionCntList = [
    Monkey0ItemsInspectedCnt,
    Monkey1ItemsInspectedCnt,
    Monkey2ItemsInspectedCnt,
    Monkey3ItemsInspectedCnt,
    Monkey4ItemsInspectedCnt,
    Monkey5ItemsInspectedCnt,
    Monkey6ItemsInspectedCnt,
    Monkey7ItemsInspectedCnt,
]

InspectionCntList.sort()
print(InspectionCntList[-1] * InspectionCntList[-2])
# print(Monkey0Items)
# print(Monkey1Items)
# print(Monkey2Items)
# print(Monkey3Items)
# print(Monkey4Items)
# print(Monkey5Items)
# print(Monkey6Items)
# print(Monkey7Items)
