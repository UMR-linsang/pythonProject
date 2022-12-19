data = {
    'login.py': 'add 8 del 2 upd 3',
    'order.py': ' add 15 del 0 upd 34',
    'info.py': ' add 1 del 20 upd 5',
    'register.py': ' add 9 del 23 upd 7',
    'exit.py': ' add 16 del 6 upd 19'
}


def get_total_changes(filename):
    # 查找该文件的变更行数
    if filename in data:
        try:
            # 拆分字符串并提取添加、删除和更新计数
            counts = data[filename].strip().split(' ')
            add, delete, update = counts[1], counts[3], counts[5]
            # 计算更改的行总数
            total_changes = int(add) + int(delete) + int(update)
            return total_changes
        except (IndexError, ValueError):
            # 如果提取计数出错，则返回0
            return 0
    else:
        return "查找的文件不存在."


# 找出每个文件更改的行总数
for filename in data:
    print(f"{filename}: {get_total_changes(filename)}")

# 从用户获取文件名
filename = input("请输入一个文件名: ")

# 查找指定文件更改的行总数
print(get_total_changes(filename))
