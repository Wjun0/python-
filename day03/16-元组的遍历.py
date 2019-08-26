my_tuple = ("青牛精", "白骨精", "蜘蛛精", "琵琶精")

# 使用for循环获取元组中的每一个数据
for value in my_tuple:
    print(value)

print("-------------------")
# 定义下标遍历，记录当前取值的下标
index = 0
while index < len(my_tuple):
    # 根据下标获取对应的数据
    result = my_tuple[index]
    print(result)

    index += 1