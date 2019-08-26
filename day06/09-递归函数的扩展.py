# 需求： 使用递归函数完成某个数字阶乘的计算

# 3! = 3 * 2 * 1 => 3 * 2!
# 2! = 2 * 1 => 2 * 1!
# 1! = 1

# 算法规则:
# n! = n * (n-1)!
import sys


# 计算某个数字的阶乘
def calc_num(n):  # n 表示要计算数字的阶乘
    # print(n)
    # 此处判断条件就是结束递归调用的条件
    if n == 1:
        return 1
    else:
        # return n * 下一个数字的阶乘
        return n * calc_num(n-1)


# 查看递归调用次数
count = sys.getrecursionlimit()
print(count)

# 设置递归调用次数
sys.setrecursionlimit(2000)

# 查看递归调用次数
count = sys.getrecursionlimit()
print(count)

result = calc_num(1000)
print("结果为:", result)
print(type(result))