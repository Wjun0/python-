person_dict = {'name': '曹丕', 'age': 49, 'sex': '男'}

# 查看字典的个数
count = len(person_dict)
print(count)

# 字典提供的相关方法--------
# 获取字典中的所有key
keys = person_dict.keys()
# 提示： 在python3里面获取字典中所有的key，返回的是dict_keys类型
# 提示： 在python2里面获取字典中所有的key，返回的是list类型
print(keys, type(keys))
# 把dict_keys转成list类型
new_keys = list(keys)
print(new_keys, type(new_keys))

# 获取字典中的所有value
values = person_dict.values()
# 提示： 在python3里面获取字典中所有的key，返回的是dict_values类型
# 提示： 在python2里面获取字典中所有的key，返回的是list类型
print(values, type(values))

# 把dict_values转成list类型
new_values = list(values)
print(new_values, type(new_values))

# 获取字典中的所有项数据
items = person_dict.items()
# 提示： 在python3里面获取字典中所有的key，返回的是dict_items类型
# 提示： 在python2里面获取字典中所有的key，返回的是list类型
print(items, type(items))
# 把dict_items转成list类型
new_items = list(items)
print(new_items, type(new_items))