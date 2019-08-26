# # 不可变类型的全局变量
# g_num = 10
#
# print("修改前g_num：", id(g_num), g_num)
#
#
# def modify_value():
#     # global本质：表示声明全局变量保存的内存地址要发生变化
#     global g_num
#     g_num = 20
#
# modify_value()
#
# print("修改后g_num：", id(g_num), g_num)

# 可变类型的全局变量
g_list = [1, 2]
print("修改前g_list：", id(g_list), g_list)


def update():
    # 此时修改数据是在原有内存空间的基础上进行修改的，全局变量的内存地址不变
    # g_list[0] = 5
    global g_list # 表示声明全局变量保存的内存地址要发生变化
    g_list = [5, 2]

update()
print("修改后g_list：", id(g_list), g_list)

# 总结：不管是可变类型的全局变量还是不可变类型的全局变量，只要对全局变量进行**重新赋值**都需要加上global
# 声明表示全局变量保存的内存地址要发生变化
