# is_ok = False
# for value1 in range(1, 4):
#     print("外层循环:", value1)
#     for value2 in range(5):
#         print("内层循环:", value2)
#         if value2 == 3:
#             is_ok = True
#             break
#
#     if is_ok:
#         break


# 简写方式：
def show():
    for value1 in range(1, 4):
        print("外层循环:", value1)
        for value2 in range(5):
            print("内层循环:", value2)
            if value2 == 3:
                # 表示内层循环要结束
                return  # 当函数执行了return表示函数执行结束，return后面即使还有更多的代码也不会执行

show()
