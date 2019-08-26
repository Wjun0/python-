# 三目运算是用来简化if - else 语句代码的
num1 = 1
num2 = 2

if num1 > num2:
    print("num1:", num1)
else:
    print("num2:", num2)

result = num1 if num1 > num2 else num2
print(result)

# 利用三目运算，判断名字是否是叫做张三，如果是叫做张三，返回找到了这个人，否则返回没有找到该人

# 接收用户输入名字

name = "张三"

if name == "张三":
    print("找到了这个人")
else:
    print("没有找到该人")

# result = "找到了这个人" if name == "张三" else "没有找到该人"
# print(result)

print("找到了这个人") if name == "张三" else print("没有找到该人")
