person_dict = {'name': '曹丕', 'age': 49, 'sex': '男'}

# 遍历字典中的每一个key
for key in person_dict.keys():
    # 打印每次获取的key值
    print(key)

print("-------------------")
# 遍历字典中的每一个value
for value in person_dict.values():
    print(value)

print("-------------------")
# 遍历字典中的每一项数据
for item in person_dict.items():
    print(item)

print("-------------------")
# 遍历字典中的每一项数据，然后获取每项数据的key和value
for item in person_dict.items():
    # print(item, type(item))
    key = item[0]
    value = item[1]
    print(key, value)

print("-------------------")
# 遍历字典中的每一项数据，然后利用拆包获取每项数据的key和value
# 拆包：使用不同变量保存容器类型中的每一个数据  ***
for key, value in person_dict.items():
    print(key, value)

my_tuple = (1, 2, 3)

# 利用拆包
value1, value2, value3 = my_tuple
print(value1, value2, value3)

print("-------------------")
# 扩展：直接变量字典，默认获取key
for key in person_dict:
    # 根据每一个key获取对应的value值
    value = person_dict[key]
    print(key, value)