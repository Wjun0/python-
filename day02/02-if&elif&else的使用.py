# 接收用户输入的年龄
age = int(input("请输入您的年龄:"))

# 根据年龄依次判断这个人是某个年龄段
# if age >= 60 and age <= 100:
#     print("老年人")
# elif age >= 40 and age < 60:
#     print("中年人")
# elif age >= 18 and age < 40:
#     print("青年人")
# else:
#     print("未成年")

# 扩展：---
if 60 <= age <= 100:
    print("老年人")
elif 40 <= age < 60:
    print("中年人")
elif 18 <= age < 40:
    print("青年人")
else:
    print("未成年")

# 注意点：当满足某个条件时，会执行对应条件语句里面的代码，当所有的添加都不满足是，会执行else语句
# else语句是可选的，根据自己的需求判断是否进行使用


# 根据用户输入的数字，判断是星期几，如果输入的不是1-7的数字请输入合法数字
# num = int(input("请输入1-7之间的一个数字:"))
#
# if num == 1:
#     print("星期一")
# elif num == 2:
#     print("星期二")
# # elif ...
# else:
#     print("请输入1-7之间的合法数字")