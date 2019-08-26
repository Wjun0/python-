# 函数的注意点:
# 1. return的注意点:
# 1.1 return只能返回1次数据
# 1.2 当函数执行return语句以后，函数会执行结束，return语句后面的代码不会执行
# 1.3 return关键字只能在函数内或者方法内使用，不能单独使用

# 2. 函数名不能重名
# 2.1 函数名相同，后面的函数会把前面的函数进行覆盖

# 3. 变量的作用域(使用范围)
# 3.1 局部变量的作用域：只能函数内
# 3.2 全局变量的作用域: 可以在不同函数内或者函数外使用


# def show():
#     print("哈哈")
#
#
# def show(msg):
#     print(msg)
#
# show('呵呵')

# def show_info():
#     # 局部变量
#     msg = "哈哈"
#     print(msg)
#
# show_info()
# print(msg)

# 定义全局变量
g_num = 1


def show():
    print(g_num)


def work():
    print(g_num)


show()
work()
print(g_num)