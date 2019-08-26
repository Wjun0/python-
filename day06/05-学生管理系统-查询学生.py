# 学生管理系统的分析
# 1. 每个学生信息可以使用字典进行存储
# 2. 系统管理不同学生可以使用列表存储

# 开发学生管理系统
# 1. 显示学生管理系统的功能菜单
# 2. 接收用户输入的功能选项
# 3. 根据功能选项完成对应的操作

# 定义全局变量
student_list = []


# 显示功能菜单
def show_menu():
    print("--------学生管理系统V1.0---------")
    print("1. 添加学生")
    print("2. 修改学生")
    print("3. 删除学生")
    print("4. 查询学生")
    print("5. 显示所有学生")
    print("6. 退出")


# 添加学生
def add_student():
    # 接收用户输入的学生信息
    name = input("请输入学生的姓名:")
    age = input("请输入学生的年龄:")
    sex = input("请输入学生的性别:")

    # 把学生信息包装到字典里面
    student_dict = dict()
    # 添加学生信息到字典
    student_dict["name"] = name
    student_dict["age"] = age
    student_dict["sex"] = sex

    # 把学生字典添加到学生列表
    student_list.append(student_dict)
    # print(student_list)


# 显示所有学生
def show_all_student():
    # 遍历学生列表，显示每一个学生信息
    for index, student_dict in enumerate(student_list):
        # 生成学号 = 下标 + 1
        student_no = index + 1
        print("学号: %d 姓名: %s 年龄: %s 性别: %s" % (student_no, student_dict["name"],
                                               student_dict["age"],
                                               student_dict["sex"]))


# 修改学生
def modify_student():
    student_no = int(input("请输入要修改学生的学号:"))
    # 生成下标 = student_no - 1
    index = student_no - 1
    # 判断是否是一个合法的下标
    if 0 <= index < len(student_list):
        # 根据下标获取要修改的字典信息
        student_dict = student_list[index]
        new_name = input("请输入您修改后的姓名:")
        new_age = input("请输入您修改后的年龄:")
        new_sex = input("请输入您修改后的性别:")
        # 修改字典的信息
        student_dict["name"] = new_name
        student_dict["age"] = new_age
        student_dict["sex"] = new_sex
    else:
        print("请输入合法的学号！")


# 删除学生
def remove_student():
    # 接收用户删除学生的学号
    student_no = int(input("请输入要删除学生的学号:"))
    # 生成下标 = student_no - 1
    index = student_no - 1
    # 判断是否是一个合法的下标
    if 0 <= index < len(student_list):
        # 根据下标删除指定数据
        del student_list[index]
        print("删除成功!")
    else:
        print("请输入合法的学号！")


# 查询学生
def query_student():
    # 接收用户输入的查询信息
    search_name = input("请输入您要查询学生的姓名:")

    # 遍历学生列表，判断是否有要查询的学生姓名
    for index, student_dict in enumerate(student_list):
        if student_dict["name"] == search_name:
            # 学号 = index + 1
            student_no = index + 1
            print("学号: %d 姓名: %s 年龄: %s 性别: %s" % (student_no, student_dict["name"],
                                                   student_dict["age"],
                                                   student_dict["sex"]))
            break
    else:
        print("对不起，您查找的学生信息不存在!")


# 程序的入口函数，程序第一个要执行的函数
def start():
    while True:
        # 显示功能菜单
        show_menu()
        # 接收用户输入的功能选项
        menu_option = input("请输入您要操作的功能选项:")

        # 判断对应的功能选项完成对应的操作
        if menu_option == "1":
            print("添加学生")
            add_student()
        elif menu_option == "2":
            print("修改学生")
            modify_student()
        elif menu_option == "3":
            print("删除学生")
            remove_student()
        elif menu_option == "4":
            print("查询学生")
            query_student()
        elif menu_option == "5":
            print("显示所有学生")
            show_all_student()
        elif menu_option == "6":
            break

# 调用函数，让学生管理系统进行工作
start()