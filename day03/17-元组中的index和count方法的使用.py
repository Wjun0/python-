# index: 获取指定数据在元组中的下标
# count: 获取指定数据在元组中出现的次数

my_tuple = ("曹操", "荀彧", "郭嘉")

# index = my_tuple.index("荀彧")
#
# print(index)

for value in my_tuple:
    # 根据数据获取对应的下标
    index = my_tuple.index(value)
    # 获取当前是第几个数据
    num = index + 1
    print(num, index, value)

print("-------------------")

result = my_tuple.count("曹昂")
print(result)