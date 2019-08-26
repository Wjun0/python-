# 集合： 也是一个容器类型，可以存储任意多个数据，集合的表现形式是一对大括号: {1, 2, 4}
# 集合的类型： set类型, 它是一个类

# 集合的特点：
# 1. 集合是无序的
# 2. 集合的数据是唯一的，不能重复
# 3. 集合也是可变类型

# 集合的注意点：
# 1. 不能通过下标获取和修改集合中的数据
# 2. 创建一个空的集合不能使用一对大括号，应该使用set()
# 3. 集合里面只能存放不可变类型

# 定义集合
my_set = {1, 2, 'a', 'b'}

print(my_set, type(my_set), id(my_set))

# 添加数据
my_set.add(0)

print(my_set, type(my_set), id(my_set))

# 测试： 添加重复的数据
my_set.add(2)

print(my_set, type(my_set), id(my_set))

# 删除数据
my_set.remove("a")
print(my_set, type(my_set), id(my_set))



# 错误写法:
# value = my_set[0]
#
# print(value)

# my_set[0] = 10

# my_set = {}
# print(my_set, type(my_set))

# 创建空的集合的正确写法
my_set = set()
print(my_set, type(my_set))
my_set.add(1)
print(my_set, type(my_set))

# 获取集合中的数据可以使用拆包或者循环

value1, value2, value3 = {1, 'b', 'c'}
print(value1, value2, value3)

for value in {1, 'b', 'c'}:
    print(value)

# 扩展：集合里面只能存储不可变类型，不能存储可变类型
my_set = {1, 2, ['a'], 'b', 5}

# 学习集合的目的: 对数据进行去重操作