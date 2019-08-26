# if嵌套：在if语句里面再次使用if语句
# if语句嵌套的格式:

# if 要判断的条件
#    if 要判断的条件
#       # 要执行的代码

# 需求： 男生找女朋友

sex = input("请输入您的性别:")

if sex == "女":
    # 代码执行到此，说明性别没有问题
    print("性别ok")

    # 性别ok以后，判断其它条件
    age = int(input("请输入您的年龄:"))

    # if age >= 18 and age <= 30:
    if 18 <= age <= 30:
        print("找到心中女神!")
    else:
        print("对不起，我们不合适!")

else:
    print("对不起，我们只要女生！")


# 接收用户输入的公交卡余额
money = float(input("请输入当前卡中余额:"))
if money > 2:
    print("上车")
    num = int(input("请输入车上空的座位数为:"))
    if num > 0:
        print("坐下")
    else:
        print("站着")

else:
    print("余额不足，请充值!")



