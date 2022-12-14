input_data = None
with open("input.txt") as input_file:
    input_data = input_file.readlines()

ans = 0
for rucksack in input_data:
    n = len(rucksack)
    first_comp = rucksack[:n // 2]
    second_comp = rucksack[-n // 2:]
    common = set(first_comp).intersection(second_comp)
    char = list(common)[0]
    if ord(char) >= 97: # small alphabets
        ans += ord(char) - 96
    else: # capital alphabets
        ans += ord(char) - 65 + 27

print(ans)
