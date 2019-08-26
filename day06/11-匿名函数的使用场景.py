# 匿名函数的使用场景:
# 1. 匿名函数可以作为参数给其他函数去使用
# 2. 匿名函数需要是配合未来学习的高级函数来使用的


# def sum_num(num1, num2):
#     return num1 + num2

# result = sum_num(1, 2)
# print(result)

# 定义函数，让该函数对传入函数进行一个功能的扩展
# print("开始计算了")
# print(3)
# print("计算结束了")


def sum_num(num1, num2):
    return num1 + num2


def show(new_func):
    print("开始计算了")
    num1 = 1
    num2 = 2
    # 调用传入过来的函数
    result = new_func(num1, num2)
    print(result)
    print("计算结束了")

# show(sum_num)

# 使用匿名函数对代码进行简化
show(lambda x, y: x + y)
