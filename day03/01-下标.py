# 下标：又称为索引，其实就是数字
# 下标的作用：就是根据下标获取数据的

# 下标的语法格式:
# my_str = "abc"
# my_str[0]  =>  变量名[下标]

# 下标可以结合range，字符串，列表，元组

my_str = "hello"

# 正数下标取值
result = my_str[3]
print(result)
# 负数下标取值
result = my_str[-2]
print(result)

# 正数下标取值
result = my_str[0]
print(result)
# 负数下标取值
result = my_str[-1]
print(result)

# 总结：在python里面下标可以分为正数下标和负数下标，下标就是用来获取数据的

# 扩展： ----
my_range = range(3)  # [0,2]
result = my_range[0]
print(result)

result = my_range[-1]
print(result)