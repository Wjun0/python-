# 切片：根据一个下标范围获取其中一部分数据，经常结合：字符串，元组，列表

# 切片的语法格式:
# 变量名[开始下标: 结束下标: 步长]
# 说明：结束下标不包含，步长默认是1

my_str = "abcdef"

# 获取字符串中的前三个数据
result = my_str[0: 3]
print(result)

# 获取字符串中的前三个数据的简写
result = my_str[:3]
print(result)

# 获取字符串中的最后三个数据
result = my_str[3:6]
print(result)

# 获取字符串中的最后三个数据的简写
result = my_str[3:]
print(result)

#
result = my_str[1: 4]
print(result)

# 使用负数下标的方式获取最后三个数据
result = my_str[-3:]
print(result)

result = my_str[-3:-1]
print(result)

# 特殊用法获取整个数据并且对字符串进行反转
result = my_str[::-1]
print(result)

print(my_str)
result = my_str[::2]
print(result)

# 总结：通过切边获取数据，如果步长是正数表示从左到右取值，如果步长是负数表示从右到左取值

my_str = "abcdef"

result = my_str[3:1:1]  # 注点意：切片指定的范围有问题，代码不会崩溃，获取的是一个空的字符串数据
print(result)

result = my_str[3:0:-1]  # 注点意：切片指定的范围有问题，代码不会崩溃，获取的是一个空的字符串数据
print(result)

# 练习：在字符串"abcdef"中获取cba数据

my_str = "abcdef"

result = my_str[2::-1] # 如果步长是负数并且结束下标不指定，表示倒着取到第一个数据

print(result)

result = my_str[-4:-7:-1]
print(result)

result = my_str[-4::-1]
print(result)

# 结束下标不指定
# 1. 步长为正数表示正着取到最后一个数据
# 2. 步长为负数表示倒着取到第一个数据
result = my_str[1::-1]
print(result)