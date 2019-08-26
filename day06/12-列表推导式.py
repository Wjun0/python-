# 列表推导式: 使用for循环快速创建一个列表，生成一个列表的

# 列表推导式的语法格式：
# [value for value in 容器类型的数据] =》 [value1, value2, .....]

# 通过列表推导式快速创建一个列表
# 需求1: [-5,..., -1]

result = [value for value in range(-5, 0)]
print(result)

# 需求2: 产生一个[1, 3, 5, 7, 9]
result = [value for value in range(1, 10, 2)]
print(result)

# 需求3：[2, 4, 6, 8] 列表推导式结合if判断来实现
result = [value for value in range(2, 9) if value % 2 == 0]
print(result)

# 使用for循环的嵌套生成元组的列表数据
result = [(x, y) for x in range(1, 4) for y in range(3)]
print(result)

# 练习题：
# 1. my_str = "ABC"  = > ["A!", "B!", "C!"]

result = [value + "!" for value in "ABC"]
print(result)

# 2. my_list = [{"name": "李四", "age": 20}, {"name": "王五", "age": 21}] , 年龄大于20的数据过滤出来放到一个列表里面

my_list = [{"name": "李四", "age": 20}, {"name": "王五", "age": 21}]

result = [my_dict for my_dict in my_list if my_dict["age"] > 20]
print(result)


# 3. my_list = [("李四", 20), ("王五", 22)]
# 通过列表推导式转成列表字典, 例如: [{"name": "李四", "age": 20}, {"name": "王五", "age": 22}]
