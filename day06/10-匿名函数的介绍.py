# 匿名函数：使用lambda关键字定义的函数称为匿名函数

# 匿名函数的特点:
# 1. 匿名函数也是属于函数，执行的时候需要加上小括号
# 2. 匿名函数只能一行代码
# 3. 匿名函数的返回值不需要加上return关键字

# 学习匿名函数的目的: 是用来简化比较简单的普通函数代码


def sum_num(num1, num2):
    return num1 + num2
#
#
# result = sum_num(2, 3)
# print(result)

# 使用匿名函数对以上代码进行简化
# 匿名函数定义的语法格式:

# lambda 形参1, 形参2...: 返回的结果或者调用其他函数


# 此时的变量名new_func 相当于一个函数名
new_func = lambda x, y: x + y  # 扩展：变量不光能够保持普通数据，还可以保存一个函数

# print(type(new_func))
#
# print(type(sum_num))

# 调用匿名函数
result = new_func(1, 2)
print(result)

# 练习题： 定义一个无参数的匿名函数，调用的时候输出hello world

new_func = lambda: print("hello world")
# new_func()
result = new_func()
print(result)