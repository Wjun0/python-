# def return_more_value():
#     print("--------1------")
#     # 注意点：当函数执行了return，表示函数执行结束，return语句后的代码不会执行
#     return 1
#     print("--------2------")
#     return 2
#     print("--------3------")
#
# # 使用变量保存调用函数后的返回值
# result = return_more_value()
# print("返回的值是:", result)

# 以上代码的问题是，无法通过多个return返回多次值，通过return只能返回一次值


# 解决办法：就是通过返回一个容器类型，完成一次性返回多个值 -------------------


def return_more_value():
    print("--------1------")
    # 注意点：当函数执行了return，表示函数执行结束，return语句后的代码不会执行
    # return [1, 2]
    # return (1, 2)
    # 返回元组简写方式
    # return 1, 2
    return {"a": 1, "b": 2}


result = return_more_value()
print(result, type(result))

