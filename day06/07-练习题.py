# 定义一个函数，能够实现传递任意多个参数并返回最大值的功能


def max_value(*args, **kwargs):

    # 把args里面的数据和kwargs里面的数据合并到一个容器类型里面
    # args # 元组
    # result = type(kwargs.values()) # dict_values
    # print(result)

    if len(args) == 0 and len(kwargs) == 0:
        return 0

    new_tuple = tuple(kwargs.values())

    result = args + new_tuple

    return max(result)


value = max_value(1, 2, 3, a=1, b=10)
print(value)