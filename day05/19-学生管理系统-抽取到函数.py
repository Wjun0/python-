# 学生管理系统的分析
# 1. 每个学生信息可以使用字典进行存储
# 2. 系统管理不同学生可以使用列表存储

# 开发学生管理系统
# 1. 显示学生管理系统的功能菜单
# 2. 接收用户输入的功能选项
# 3. 根据功能选项完成对应的操作


# 显示功能菜单
def show_menu():
    print("--------学生管理系统V1.0---------")
    print("1. 添加学生")
    print("2. 修改学生")
    print("3. 删除学生")
    print("4. 查询学生")
    print("5. 显示所有学生")
    print("6. 退出")


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
        elif menu_option == "2":
            print("修改学生")
        elif menu_option == "3":
            print("删除学生")
        elif menu_option == "4":
            print("查询学生")
        elif menu_option == "5":
            print("显示所有学生")
        elif menu_option == "6":
            break

# 调用函数，让学生管理系统进行工作
start()