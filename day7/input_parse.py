from collections import defaultdict

commands = ["cd", "ls"]

class Node:
    def __init__(self, size = 0, name = ""):
        self.size = size
        self.name = name
        self.childs = {}
        self.files = {}

    def __repr__(self):
        files = ", ".join(map(str, self.files.keys()))
        childs = ", ".join(map(str, self.childs.keys()))
        return f"""name: {self.name}, size: {self.size}, childs={[childs]}, files={[files]}"""

stack = []
cur = None
root = None
def get_tree():
    global cur, root, stack
    with open("input.txt") as inp:
        for line in inp.readlines():
            if line[0] == "$": # it is a command
                command = line[2:4]
                if command == "cd": # it has argument
                    arg = line[5:][:-1]
                    if arg == "..": # move back
                        cur = stack[-1]
                        stack.pop()
                    elif arg == "/":
                        cur = Node(name="/")
                        root = cur
                    else:
                        if arg not in list(map(str, cur.childs.keys())):
                            cur.childs[arg] = Node(name=arg)
                        stack.append(cur)
                        cur = cur.childs[arg]
                        # print(f"cur = {cur}", f"stack = {stack}")

            elif  ord(line[0]) >= 48 and ord(line[0]) <= 57: # it is a file listing
                size, filename = line.split(" ")
                cur.files[filename[:-1]] = int(size)
            else: # it is a directory listing
                dirname = line[4:-1]
                # add dir listing to current node
                if dirname not in list(map(str, cur.childs.keys())):
                    cur.childs[dirname] = Node(name=dirname)
            # print(stack)
        return root
