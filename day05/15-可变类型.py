# 可变类型：允许在原有内存空间的基础上修改数据，修改后变量保存的内存地址不变

# 可变类型有： 列表，字典，集合

my_list = [1, 3, 5]

print("修改前my_list:", id(my_list), my_list)

# 添加数据
my_list.append(7)

print("修改后my_list:", id(my_list), my_list)

my_list.remove(3)

print("修改后my_list:", id(my_list), my_list)


my_dict = {"name": "李四"}

print("修改前my_dict:", id(my_dict), my_dict)

my_dict["name"] = "王五"

print("修改后my_dict:", id(my_dict), my_dict)

print("-------------------")
# 扩展：对可变类型的变量进行重新赋值
my_list = [1, 2, 3]

print("修改前my_list:", id(my_list), my_list)

my_list = [4, 5, 6]
print("修改后my_list:", id(my_list), my_list)

# 总结:
# 对于可变类型来说，修改数据可以有两种方式来完成
# 1. 在原有内存空间的基础上进行修改，此时变量保存的内存地址不会发生变化
# 2. 通过重新赋值来进行修改，此时变量保存的内存地址会发生变化

# 练习题:

a = [1, 2]
b = a

# a.append(3)
a = [3, 5]

# a的数据和b的数据分别是什么
print(a, b)


