import os


# 1. 获取指定目录下的所有文件名
file_name_list = os.listdir("CCC")

path = os.getcwd()
print(path)
# 切换目录
os.chdir("CCC")
path = os.getcwd()
print(path)
# 2. 遍历获取的文件名列表，依次对每一个文件进行重命名
for file_name in file_name_list:
    # 生成重命名后的文件名 = "[彬哥出品]-" + file_name
    new_file_name = "[彬哥出品]-" + file_name
    print(file_name, new_file_name)

    # 调用重命名方法，完成重命名操作
    # 问题：现在操作的目录是day07，而重命名的文件在CCC目录里面
    # 解决办法：
    # 1. 拼接路径，给重命名的文件加上CCC目录名
    # os.rename("CCC/" + file_name, "CCC/" + new_file_name)
    # 2. 切换到CCC目录以后再进行重命名操作
    os.rename(file_name, new_file_name)