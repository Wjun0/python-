def show(params):  # params = my_tuple（my_list）
    # 在python里面所有的赋值操作都是按照引用传递的，按照引用传递通俗理解就是按照内存地址进行传递
    print("params:", id(params), params)

    # 对参数进行+=操作，
    # +=的本质：在params原有内存空间的基础上修改数据
    # 提示: 如果params这个参数是一个不可变类型，那么+=后，这个params变量保存的内存地址会发生变化
    # params += params

    # 提示: 如果params这个参数是一个可变类型，那么+=后，这个params变量保存的内存地址不会发生变化
    # params += params

    print("修改后params:", id(params), params)


# 定义不可变类型的变量
# my_tuple = (1, 2)
#
# print("my_tuple:", id(my_tuple), my_tuple)
#
# show(my_tuple)

# 定义可变类型的变量
my_list = [1, 2]

print("my_list:", id(my_list), my_list)

show(my_list)
