# +	[1, 2] + [3, 4]	[1, 2, 3, 4]	合并	字符串、列表、元组
# *	['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	复制	字符串、列表、元组
# in	3 in (1, 2, 3)	True	元素是否存在	字符串、列表、元组、字典
# not in	4 not in (1, 2, 3)	True	元素是否不存在	字符串、列表、元组、字典

# + ：可以进行计算和合并
num1 = 1
num2 = 2

result = num1 + num2
print(result)

my_str1 = 'abc'
my_str2 = 'bcd'
# 合并操作
result = my_str1 + my_str2
print(result)

my_list1 = [1, 2]
my_list2 = [3, 4]
result = my_list1 + my_list2 # 使用变量保存两个列表合并后的结果
print(result, type(result))

my_tuple1 = (1, 2)
my_tuple2 = (3, 4)
result = my_tuple1 + my_tuple2 # 使用变量保存两个列表合并后的结果
print(result, type(result))

print("-----------------------")

# * ：可以进行计算和复制
num1 = 2
num2 = 3

# 完成数字计算操作
result = num1 * num2
print(result)

# 完成对容器类型中的数据进行复制操作
my_str = "ab"
new_str = my_str * 2
print(new_str)

my_list = [1, 2]
result = my_list * 3

print(result)

my_tuple = ("AA", "CC")
result = my_tuple * 2

print(result)

# in 和 not in 的使用
my_str = "abcedf"

result = "ce" in my_str
print(result)

result = "cd" in my_str
print(result)

my_tuple1 = (1, 2)

result = 1 in my_tuple1
print(result)

result = 3 in my_tuple1
print(result)

person_dict = {'name': '曹丕', 'age': 49, 'sex': '男'}

result = "男" in person_dict.values()  # 默认判断key
print(result)

result = "name" in person_dict  # 默认判断key
print(result)

print("-" * 30)


# 在程序中定义一个变量，存储一个人的基本信息(姓名，年龄，阅读的书籍有: 三国演义，西游记)

# 再添加一个阅读的书籍：红楼梦

# 打印这个人的基本信息，格式如下:

# 姓名: 张三 年龄: 20 阅读书籍有: 三国演义，西游记，红楼梦













