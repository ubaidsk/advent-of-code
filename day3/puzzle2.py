input_data = None
with open("input.txt") as input_file:
    input_data = input_file.readlines()

ans = 0
for i in range(0, len(input_data), 3):
    rucksack1, rucksack2, rucksack3 = input_data[i], input_data[i + 1], input_data[i + 2]
    common = set(rucksack1.strip()).intersection(set(rucksack2.strip()))
    common = common.intersection(set(rucksack3.strip()))
    char = list(common)[0]
    # print(common)
    if ord(char) >= 97: # small alphabets
        ans += ord(char) - 96
    else: # capital alphabets
        ans += ord(char) - 65 + 27

print(ans)
