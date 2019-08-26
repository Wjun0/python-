import os  # 操作文件和文件夹的模块
import shutil # 操作文件和文件夹的高级模块

# 1. 创建一个空的文件,文件名叫做AA.txt
# file = open("AA.txt", "wb") # 默认把文件创建到当前工程目录里面
# file.close()

# 2. 重命名
# 1. 原文件的名字
# 2. 修改后的名字
# os.rename("AA1.txt", "aa.txt")

# 3. 删除指定文件
# os.remove("aa.txt")

# 4. 创建空的目录(文件夹)
# os.mkdir("AAA")
# 把文件创建到指定目录，加上对应的路径即可
# file = open("AAA/aa.txt", "wb") # 默认把文件创建到当前工程目录里面
# file.close()

# os.remove("AAA/aa.txt")

# file = open("AAA/aa.txt", "wb") # 默认把文件创建到当前工程目录里面
# file.close()
#
# file = open("AAA/bb.txt", "wb") # 默认把文件创建到当前工程目录里面
# file.close()

# 5. 获取指定目录下的所有文件名
# file_name_list = os.listdir("AAA")
# print(file_name_list)

# 6. 获取当前操作目录的路径
path = os.getcwd()
print(path)

# 获取当前目录下的所有文件名
file_name_list = os.listdir(".")
print(file_name_list)

# 7. 切换目录
# os.chdir("AAA")

path = os.getcwd()
print(path)

# 获取当前目录下的所有文件名
file_name_list = os.listdir(".")
print(file_name_list)


# os.mkdir("BBB")

# 8. 删除空的目录
# os.rmdir("BBB")

# 切换到上一级目录
# os.chdir("..")

path = os.getcwd()
print(path)

# 扩展：
# 1. 删除非空目录

# os.rmdir("AAA")
# shutil.rmtree("AAA")
# 2. 判断文件是否存在
result = os.path.exists("1.png")
print(result)
result = os.path.exists("AA/777.txt")
print(result)

# 3. 判断文件夹是否存在
result = os.path.exists("AA")
print(result)

# 4. 判断是否是一个文件
result = os.path.isfile("AA/666.txt")
print(result)
# 5. 判断是否是一个文件夹
result = os.path.isdir("AA")
print(result)

# 6. 获取指定路径的文件名
file_name = os.path.basename("A/B/1.txt")
print(file_name)
# 7. 获取指定路径的文件夹的路径
path = os.path.dirname("A/B/1.txt")
print(path)

# 8. 可以对文件进行分割，获取文件名和文件的后缀, "1.txt" -> 1  .txt
file_name, end_str = os.path.splitext("1.txt")
print(file_name, end_str)


# 1. 根据用户输入的文件名，对文件进行拷贝，拷贝后的名字是在原文件的基础上加上[复件],
# 比如： 1.txt -> 1[复件].txt