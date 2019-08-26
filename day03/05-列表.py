# 列表：其实就是一个数据的容器，可以存储多个数据，列表的表现形式: [1,4,...]
# 注意点：列表可以存放任意类型的数据
# 列表的类型: list

my_list = [1, 3.14, True, 'abc', range(5)]
print(my_list, type(my_list))

# 根据下标获取列表中的某个数据
result = my_list[-1]
# range类型： 范围
print(result, type(result))

result = my_list[1]
print(result, type(result))

# 根据切片获取其中一部分数据
result = my_list[1:4]
print(result)

result = my_list[-3:]
print(result)

result = my_list[:3]
print(result)