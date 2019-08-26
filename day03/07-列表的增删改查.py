# 创建空列表的两种方式
# my_list = []  # 定义空的列表
# my_list = list() # 定义空的列表
# 这个警告是表示创建列表让你使用: list()
# my_list = ["曹操", "刘备", "孙权"]

my_list = list(("曹操", "刘备", "孙权"))
print(my_list)

# 添加操作------------
# 追加数据
my_list.append("夏侯惇")
print(my_list)
# 插入数据
my_list.insert(2, "刘表")
print(my_list)
name_list = ["乐进", "于禁"]
# my_list.append(name_list)
# print(my_list)
# extend: 扩展一组数据，把指定列表中的每一个数据添加到相应列表
my_list.extend(name_list)
print(my_list)

# 修改数据操作----------------
my_list[0] = "曹阿满"
print(my_list)

my_list[1] = "刘皇叔"
print(my_list)

my_list[-1] = "小于"
print(my_list)

# 扩展： 根据切片修改多个数据
my_list[-3:] = ["曹真", "曹仁", "曹植"]
print(my_list)

# 删除数据操作-------------
del my_list[1]
print(my_list)

# 扩展： 根据切片删除多个数据
del my_list[-3:]
print(my_list)

del my_list[0:3:2]
print(my_list)

# 查看数据
result = my_list[0]
print(result)