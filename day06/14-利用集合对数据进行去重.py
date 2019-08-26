my_list = [1, 2, 3, 1]

# 可以把列表转成集合
new_set = set(my_list)

print(new_set, type(new_set))

# 为了操作数据更加方便，可以把集合转成列表
new_list = list(new_set)
print(new_list, type(new_list))

my_tuple = ('A', 'a', "A", 1)

# 把元组转成set类型
new_set = set(my_tuple)
print(new_set, type(new_set))

# 把集合转成元组
new_tuple = tuple(new_set)
print(new_tuple, type(new_tuple))

# 提示： 元组，列表，集合三者之前可以相互进行类型转换
my_list = [1, 2, 3, 1]
new_tuple = tuple(my_list)
print(new_tuple, type(new_tuple))

new_list = list(new_tuple)

print(new_list, type(new_list))

# 总结： 集合可以把元组和列表中的数据进行去重

my_str = "AABBCC"
result = set(my_str)
print(result, type(result))

new_str = str(result)
print(new_str, type(new_str))

# 把集合转成字符串
new_str = "".join(result)

print(new_str, type(new_str))

# 字符串转列表
my_str = "AABBCC"
result = list(my_str)
print(result)
print("------------------")
my_list = ['A', 'A', 'B', 'B', 'C', 'C']

# new_str = str(my_list)  # = > "['A', 'A', 'B', 'B', 'C', 'C']"
# print(new_str, type(new_str))

result = "".join(my_list)
print(result)

# 总结：把列表，元组，结合转成字符串，不要使用str，使用.join方法

