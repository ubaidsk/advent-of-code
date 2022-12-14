from input_parse import get_tree

root = get_tree()

sum_of_dirs_of_size_atmost_100000 = 0

def dfs(cur):
    global sum_of_dirs_of_size_atmost_100000
    summ = sum(cur.files.values())
    for key in cur.childs.keys():
        summ += dfs(cur.childs[key])
    if summ <= 10 ** 5:
        sum_of_dirs_of_size_atmost_100000 += summ
    return summ

dfs(root)

print(sum_of_dirs_of_size_atmost_100000)
