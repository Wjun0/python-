# 不可变类型：不允许在原有内存空间的基础上修改数据，修改后变量保存的内存地址会发生变化

# 不可变类型有: 数字，字符串，元组

my_num = 100

print("修改前my_num:", id(my_num), my_num)

# 提示：数字不能在原有内存空间的基础上修改数据，修改数据只能通过重新赋值
# my_num[0] = 2
my_num = 200

print("修改后my_num:", id(my_num), my_num)

my_str = "hello"
print("修改前my_str:", id(my_str), my_str)
# my_str[1] = "x"

# 可以通过重新赋值来完成数据的修改
my_str = "hxllo"

print("修改后my_str:", id(my_str), my_str)

# 总结： 不可变类型，不能在原有内存空间的基础上修改数据，只能通过重新赋值来完成，这样变量保存的内存地址会发生变化


