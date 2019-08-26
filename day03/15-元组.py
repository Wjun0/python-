# 元组：好比是一个只读的列表，只读获取元组中的数据，不能对元组进行修改（添加、删除、修改）

# 元组的表现形式: (1, 1.5)

# 元组也是一个容器类型，可以存储任意类型的数据

# 定义元组
my_tuple = (1, 1.5, True, "abc", [1, 4], range(5))
print(my_tuple, type(my_tuple))

# int, float, bool, str, range, list, tuple 都是类(class)

# 对元组进行操作
result = my_tuple[0]
print(result)

result = my_tuple[-2]
print(result)

# 扩展：元组可以结合切片使用
result = my_tuple[: 3]
print(result)

result = my_tuple[-3:]
print(result)

# 错误操作: 不允许对元组进行修改
# my_tuple[1] = 5
# del my_tuple[0]

# 元组的使用的注意点：如果元组里面只有一个元素，那么这个逗号不能省略
my_tuple1 = (1, )
print(my_tuple1, type(my_tuple1))

# 元组使用的场景：
# 1. 函数的返回值是一个元组
# 2. 格式化输出的时候，多个参数放到了元组里面
print("%s %d" % ('abc', 5))
