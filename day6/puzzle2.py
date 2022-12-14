with open("input.txt") as inp:
    s = inp.read()
    for i in range(len(s) - 13):
        unique_chars = set(s[i:i + 14])
        if len(unique_chars) == 14:
            print(i + 14)
            exit(0)
