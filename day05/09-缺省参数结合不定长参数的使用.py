# def show(name, age, sex="男", *args):
#     print("name:", name, "age:", age, "sex:", sex, "args:", args)


# show("李四", 20, "男", 1, 2, 3)
# show("李四", 20, 1, 2, 3)

# 注意点：不定长位置参数和缺省参数结合使用，缺省参数需要放到不定长位置参数的后面
def show(name, age, *args, sex="男"):
    print("name:", name, "age:", age, "sex:", sex, "args:", args)

# show("李四", 20, 1, 2, 3, 3, 4, 5, 56)

# show("李四", 20, 1, 2, 3, 3, 4, 5, 56, "女")
#
# show("李四", 20, 1, 2, 3, 3, 4, 5, 56, sex="女")


# 注意点：**kwargs结合其它参数一起使用的时候，该参数需要放到所有参数的最后面
def show(name, age, *args,  sex="男", **kwargs):
    print("name:", name, "age:", age, "sex:", sex, "args:", args, "kwargs:", kwargs)


# show("王美丽", 18, 1, 2, 3, sex="女", a=1, b=2, c=3)
show("王美丽", 18, 1, 2, 3, a=1, b=2, c=3)


# 总结：
# 1. 不定长位置参数和缺省参数结合使用，缺省参数需要放到不定长位置参数的后面
# 2. **kwargs结合其它参数一起使用的时候，该参数需要放到所有参数的最后面

# 练习题：

# 1. 定义一个函数，能够实现任意多个数字的乘法计算
def calc_num(*args, **kwargs):

    result = 1
    for value1 in args:
        result *= value1

    for value2 in kwargs.values():
        result *= value2

    # 当位置参数和关键字参数都没有的时候，结果设置为0
    if len(args) == 0 and len(kwargs) == 0:
        result = 0

    return result

value = calc_num(1, 2, a=2, b=3)
print(value)

value = calc_num()
print(value)

# 2. 定义一个函数，能够实现传递任意多个参数并返回最大值的功能








