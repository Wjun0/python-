# import functools
from functools import reduce # 从functools模块导入reduce函数

# 1. reduce：根据函数的功能对容器类型中的每一个数据完成相关计算
# 2. filter：根据函数的功能对容器类型中的每一个数据进行过滤

my_list = ['A', 'B', 'C']


# def join_str(str1, str2):
#     return str1 + str2

# 1. 功能函数
# 2. 容器类型的数据
# result = reduce(join_str, my_list)
# print(result, type(result))

# 使用匿名函数对代码进行简化
result = reduce(lambda x, y: x + y, my_list)

print(result, type(result))


my_tuple = (1, 2, 3, 4, 5)

# def my_filter(x):
#     return x % 2 == 1

# 1. 功能函数
# 2. 容器类型的数据
# 返回的是过滤结果的对象
new_filter = filter(lambda x: x % 2 == 1, my_tuple)
print(new_filter, type(new_filter))
# 对过滤结果对象进行类型转换(元组)
result = tuple(new_filter)
print(result, type(result))

# 总结： 匿名函数一般都是结合高阶函数来使用
# reduce这个高阶函数需要的函数有两个参数
# filter这个高阶函数需要的函数有一个参数

# 1. 使用reduce计算1-100之间的数字的和
# reduce(功能函数, 容器类型的数据)
result = reduce(lambda x, y: x + y, range(1, 101))
print(result)
# 2. 使用filter过滤年龄大于20的数据，my_list = [{"name": "李四",  "age": 20}, {"name": "王五",  "age": 22}]

my_list = [{"name": "李四",  "age": 20}, {"name": "王五",  "age": 22}]
new_filter = filter(lambda my_dict: my_dict["age"] > 20, my_list)
result = list(new_filter)
print(result)
