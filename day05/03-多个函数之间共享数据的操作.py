# 多个函数之间共享数据的操作

# 1. 使用全局变量
# 2. 返回值


# 定义全局变量
g_num = 0


def modify_value():
    global g_num
    g_num = 10
    print("modify_value函数 全局变量修改后的数据为:", g_num)


def show():
    print("show函数 访问全局变量:", g_num)


modify_value()
show()


# 函数的返回值，可以在不同函数之间共享数据 -----------

def return_value():
    msg = "hello"
    return msg


def show_msg():
    # 使用变量保存调用函数后的返回值
    result = return_value()
    print("show_msg:", result)


show_msg()


def show_info():
    result = return_value()
    print("show_info:", result)

show_info()

# 总结： 以上多个函数之间共享数据的操作，利用返回值共享数据的方式使用的居多
