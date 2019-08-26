a = 4
b = 5

print(a, b)

# 所有语言共有的写法: 使用第三个变量临时存储某个变量的值
#
# c = a
#
# a = b
#
# b = c
#
# print(a, b)

# python的特有写法，交换两个变量的值
# a, b = b, a
# print(a, b)

# result = b, a
# print(result, type(result))
#
# a, b = result
# print(a, b)

# 简写方式

a, b = b, a  # 先把b和a的数据包装到了一个元组里面，然后使用拆包保存元组中的每一个数据，实现交换两个变量值的功能
print(a, b)
