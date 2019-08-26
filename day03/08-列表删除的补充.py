my_list = ["王熙凤", "薛宝钗", "贾宝玉"]

# 如果不指定参数，默认使用pop删除的是最后一个元素
# result = my_list.pop()
# print(result)
# print(my_list)

result = my_list.pop(1)
print(result)
print(my_list)

# remove删除列表中的指定数据
my_list.remove("王熙凤1")
print(my_list)
