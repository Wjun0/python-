# 不定长参数: 参数的个数不确定，可能使用0个或者1个或者多个参数

# 不定长参数可以分为:
# 1. 不定长位置参数, *args 表示该参数可以接收不定长位置参数，
# 1.1 注意点：在定义函数的时候，只要给参数名前面加上一个星花，那么该参数就是不定长参数
# 2. 不定长关键字参数, **kwargs 表示该参数可以接收不定长关键字参数
# 2.1 注意点： 在定义函数的时候，只要给参数名前面加上两个星花， 那么该参数就是不定长关键字参数


# *args ：这个参数名可以进行修改，但是一般都不需要进行修改使用args即可
# *args ：这个参数名可以进行修改，但是一般都不需要进行修改使用kwargs即可
def sum_num(*args, **kwargs):
    # args: 调用函数时把所有的位置参数包装成一个元组，赋值给args这个参数， args是一个元组类型
    print("args:", args)
    # kwargs: 调用函数时把所有的关键字参数包装成一个字典，赋值给kwargs这个参数，kwargs是一个字典类型
    print("kwargs:", kwargs)
    # 计算多个数据的类
    result = 0

    # 遍历元组
    for value in args:
        # print(value)
        result += value

    # 遍历字典
    for value in kwargs.values():
        result += value

    # 代码执行到此，说明位置参数的和计算完成
    return result

# 使用位置参数的方式进行传参
# value = sum_num(1, 2)
# print("结果为:", value)
# value = sum_num(a=1, b=2)
# print("结果为:", value)

num = sum_num(1, 2, a=1, b=4)
print("结果为:", num)

num = sum_num()
print("结果为:", num)