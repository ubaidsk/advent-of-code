from input_parse import get_tree

root = get_tree()


def dfs(cur):
    summ = sum(cur.files.values())
    for key in cur.childs.keys():
        summ += dfs(cur.childs[key])
    cur.size = summ
    return summ

max_size = 7 * 10 ** 7
req_space = 3 * 10 ** 7
min_suitable_dir = root
total_used_space = dfs(root)
total_unused_space = max_size - total_used_space
min_dir_size_to_delete = req_space - total_unused_space

def find_suitable_dir(cur):
    global min_dir_size_to_delete, min_suitable_dir
    for key in cur.childs.keys():
        find_suitable_dir(cur.childs[key])
    if cur.size >= min_dir_size_to_delete:
        if cur.size < min_suitable_dir.size:
            min_suitable_dir = cur

find_suitable_dir(root)

print(min_suitable_dir.size)
