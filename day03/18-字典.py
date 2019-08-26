# 字典：也是一个容器类型，可以存储多个键值对数据
# 字典的表现形式： {key: value, ....}
# 字典的场景：对于描述性信息使用字典进行存储， 比如：学生信息，老师信息等等

my_dict = {"sex": "男", "name": "曹操", "age": 66, "address": "北京"}
print(my_dict, type(my_dict))

# 中括号方式获取字典中的数据------------
# 获取数据，根据key获取对应的value值
result = my_dict["name"]
print(result)
# 错误：中括号访问如果key在字典里面不存在，程序会崩溃
# result = my_dict["address"]
# print(result)

# get方法获取字典中的数据
sex = my_dict.get("sex")

print(sex)

# get方式获取数据，如果key不存在获取的是None
# address = my_dict.get("address")
#
# print(address)

# get方式获取数据，如果key不存在获取的是None
address = my_dict.get("address", "上海")

print(address)

# 注意点：字典中的key是唯一，不能重复

my_dict = {"name": "曹操", "age": 66, "sex": "男", "address": "北京", "age": 99}
print(my_dict)