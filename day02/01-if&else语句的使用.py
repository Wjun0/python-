# 需求：根据用户输入的年龄，判断人是否成年

age = int(input("请输入您的年龄:"))

if age >= 18:
    # 条件成立，会执行if语句
    print("哥成年了，可以进入网吧肆无忌惮的玩耍!")
else:
    # 条件不成立，会执行else语句
    print("对不起，再忍几年吧！")


# 接收用户的身高
height = int(input("请输入您的身高(cm):"))

if height <= 150:
    print("不用买票")
else:
    print("需要买票")
