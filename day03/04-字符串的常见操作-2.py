# 1. find：根据指定数据获取对应的下标
my_str = "hello"

# 1. 要查找的指定字符串数据
# 2. 开始下标
# 3. 结束下标(不包含)
# 注意点：如果数据没有找到返回的数据是-1, 不是表示最后一个数据
index = my_str.find("e", 0, 2)
print(index)

# 2. index：根据指定数据获取对应的下标, 注意点：如果没有找到对应的数据直接崩溃

# 1. 要查找的指定字符串数据
# 2. 开始下标
# 3. 结束下标(不包含)
index = my_str.index("o", 3, 6)

print(index)

# index = my_str.index("x")
#
# print(index)

# 3. count：统计指定数据出现次数
my_str = "hello"
result = my_str.count("l")
print(result)
# 1. 要统计的字符串
# 2. 开始下标
# 3. 结束下标(不包含)
result = my_str.count("l", 0, 3)
print(result)

result = my_str.count("x", 0, 3)
print(result)

# 4. replace：替换 , 注意: 替换完成后会返回一个新的字符串数据
new_str = my_str.replace("l", "w")
print(new_str)
# 1. 要替换的字符串
# 2. 替换后的字符串
# 3. 替换的次数，默认是count=-1，-1：表示全部替换
new_str = my_str.replace("l", "w", 1)
print(new_str)

# 5. split ： 根据指定字符串进行分割数据
my_str = "苹果,榴莲,山竹,车厘子"
# 1. 指定分割数据的字符串
# 2. 分割次数， maxsplit=-1 ,全部进行分割
result = my_str.split(",", 1)
print(result)

# 6. startswith : 判断是否是以指定字符串开头
my_url = "http://www.baidu.com"
result = my_url.startswith("https://")
print(result)

# 7. endswith: 判断是否是以指定字符串结尾
result = my_url.endswith("m")

print(result)

# 8 strip: 去除两边空格
my_str = "  abc  "
print(my_str)
result = my_str.strip()
print(result)

# 扩展：去除指定数据
my_str = "abc,"
result = my_str.strip(",")

print(result)

my_str = "hello world"
# 9. rfind: 从右往左查找数据对应的下标
index = my_str.rfind("o")
print(index)

# 10. partition: 根据指定数据分割成三部分

file_name = "1.txt"
# 根据指定数据分割成三部分，返回的是一个元组
result = file_name.partition(".")

print(result)

# 11. splitlines: 根据换行符进行分割数据
my_str = "hello\nworld"
result = my_str.splitlines()
print(result)

result = my_str.split("\n")
print(result)

# 12. isdigit: 判断数据是否都是数字组成
my_str = "123"
result = my_str.isdigit()
print(result)

# 13. join: 根据指定字符串把容器类型中的每个字符串数据进行拼接，返回的是一个新的字符串

my_str = "abc"  # "a,b,c"

# 对容器类型中的每个字符串数据进行拼接
result = ",".join(my_str)

print(result)

# 扩展： 对列表中的每个字符串数据进行拼接
my_list = ['1', '2', '3']
result = "!".join(my_list)
print(result, type(result))