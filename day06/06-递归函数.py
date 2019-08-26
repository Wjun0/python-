# 递归函数：在一个函数里面有调用了函数本身，该函数称为递归函数

# 递归函数的注意点：**递归函数必须要有结束递归调用条件**

# def show_msg():
#     print("我是一个无参数无返回值的函数")
#
#
# def show():
#     print("show函数开始执行了")
#     # 调用其他函数
#     show_msg()
#     print("show函数执行结束了")
#
# show()


# 递归函数的写法
def show(num):
    print("哈哈")
    # 此次的条件就是结束递归调用的条件
    if num == 1:
        print("over")
    else:
        # 在函数内部调用函数本身，这样就会产生递归调用
        show(num-1)

show(3)
