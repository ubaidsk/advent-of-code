with open("input.txt") as inp:
    s = inp.read()
    for i in range(len(s) - 3):
        unique_chars = set(s[i:i + 4])
        if len(unique_chars) == 4:
            print(i + 4)
            exit(0)
