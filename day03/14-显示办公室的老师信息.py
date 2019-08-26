import random

# 1. 定义老师列表， 办公室列表
teacher_list = ["于老师", "郭老师", "孙老师", "惠老师", "李老师", "马老师", "牛老师", "杨老师"]
# office1 = []
# office2 = []
# office3 = []
# 每个办公室就是一个列表
office_list = [[], [], []]

# 2. 遍历老师列表，把每一个老师随机添加到某一个办公室
for teacher in teacher_list:
    # 生成随机办公室下标
    index = random.randint(0, 2)
    print(teacher, index)

    # 获取指定的办公室，添加对应的老师
    office_list[index].append(teacher)

# 3. 查看办公室的老师信息
# 遍历办公室列表，获取每一个办公室
num = 1  # 记录当前遍历时第几个办公室
for office in office_list:
    # print(office, num)
    # 获取每个办公室的老师个数
    result = len(office)
    print("第%d个办公室的人数为: %d" % (num, result))
    # 遍历办公室显示每一位老师信息
    for teacher in office:
        print(teacher)

    num += 1