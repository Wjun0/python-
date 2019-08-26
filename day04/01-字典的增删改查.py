my_dict = {"name": "曹丕", "age": 49, "sex": "男"}
print(my_dict)

# 添加数据, 注意点: 操作的key在字典中不存在时添加键值对操作
my_dict["address"] = "安徽"
print(my_dict)

# 修改数据，注意点：操作的key在字典中存在时表示修改数据操作
my_dict["age"] = 69
print(my_dict)

# 删除数据
del my_dict["sex"]
print(my_dict)

# 获取字典中的数据
name = my_dict.get("name")
print(name)
age = my_dict["age"]
print(age)

# 清除字典中的所有数据
my_dict.clear()
print(my_dict)

# 定义空的字典可以使用: {} 或者 dict()

# 扩展： 清除列表中的所有数据
my_list = [1, 2, 3]
my_list.clear()
print(my_list)

# 扩展：创建字典的时候，可以通过dict类型创建
my_dict = dict(name="张三", height=1.8, sex="男")
print(my_dict)

# 合并字典  -扩展
my_dict1 = {"name": "曹丕", "age": 49, "sex": "男"}
my_dict2 = {"address": "安徽", "job": "君主", "sex": "女"}
print(my_dict1)

# 把字典2中的每个键值对数据添加到字典1里面
my_dict1.update(my_dict2)

print(my_dict1)

# 扩展：----
# 练习题：定义一个男生信息的字典，然后给它添加一个女朋友的字典信息。
boy_dict = {"name": "张三", "sex": "男", "age": 20}

boy_dict["girl"] = {"name": "王美玲", "sex": "女", "age": 22}

print(boy_dict)


boy_dict["girl"]["age"] = 18

print(boy_dict)











