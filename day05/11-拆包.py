# 拆包：使用不同变量对容器类型(字符串，列表，元组，字典，集合，range)中的每一个数据进行保存
# 注意点：拆包使用结合容器类型使用

# a,b,c = 123 # 错误写法

my_str = "abc"

# 注意点：变量的个数要和容器类型中数据的个数保持一致
my_str1, my_str2, my_str3 = my_str
print(my_str1, my_str2, my_str3)

my_dict = {"name": "李四", "age": 20}

# 直接对字典进行拆包获取的是key
# value1, value2 = my_dict
# print(value1, value2)

# value1, value2 = my_dict.values()
# print(value1, value2)

# 拆包的使用场景:


def return_value():
    return 1, 2, 3

# 对函数的返回值（容器类型）进行拆包
v1, v2, v3 = return_value()
print(v1, v2, v3)


# 拆包练习:
my_value = (1, (1, 2))

result1, result2 = my_value
print(result1, result2)

# 拆包：使用不同变量保存容器类型中的每一个数据
a, b = [1, 4]

