# 缺省参数: 形参设置了默认值，那么该参数就是缺省参数

# 缺省参数的特点:
# 1. 当调用函数的时候给缺省参数传值了，那么就是使用传入的数据
# 2. 当调用函数的时候没有给缺省参数传值，那么就是使用默认值

# 注意点：
# 1. 缺省参数后面不能再跟上非缺省参数
# 2. 缺省参数后面可以在跟上缺省参数


def sum_num(num1, num2=10, num3=1, num4=1):  # 此时num2 就是缺省参数
    result = num1 + num2
    return result


# value = sum_num(1, 2)
#
# print(value)

value = sum_num(1)

print(value)


def show(name, age, sex="男"):
    print(name, age, sex)

show("张三", 18)