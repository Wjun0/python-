def show(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


my_tuple = (1, 2)
my_dict = {"a": 1, "b": 4}

# 按照位置参数的方式进行传参，表示这个两个参数都是给args
# show(my_tuple, my_dict)

# 扩展：把元组按照位置参数方式进行传参，把字典按照关键字参数的方式进行传参

# show(1, 2, a=1, b=4)

# 对元组进行拆包，把元组中的每一个数据按照位置参数的方式进行传参
show(*my_tuple)  # => show(1, 2)
# 对字典进行拆包，把字典中的每一个数据按照关键字参数的方式进行传参
show(**my_dict)  # => show(a=1, b=2)

show(*my_tuple, **my_dict) # => show(1, 2, a=1, b=2)

# 注意点： *my_tuple, **my_dict 不能单独使用，只能结合函数使用

# 练习题:

my_dict = {"name": "李四", "age": 20}


def show(name, age):
    print(name, age)

# 如何把字典中的每项数据给函数的参数(name, age)
# 把字典中的数据按照关键字的方式进行传参
show(**my_dict) # => show(name="李四", age=20)

# 练习题2：
print("---------------")


def show_msg(*args, **kwargs):
    print("show_msg args:", args)
    print("show_msg kwargs:", kwargs)


def show(*args, **kwargs):
    print("show args:", args)
    print("show kwargs:", kwargs)
    # args:表示一个元组
    # kwargs:表示一个字典
    show_msg(*args, **kwargs)


my_tuple = (1, 2)
my_dict = {"a": 1, "b": 4}

show(*my_tuple, **my_dict)






