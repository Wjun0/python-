# rb模式： 以二进制(字节)的方式读取文件中的数据

# 学习rb模式的目的是: 为了以后可以兼容读取图片、视频、音频等格式的数据， r模式只能读取文本文件中的数据

# # 第一步：打开文件,
# file = open("1.png", "rb")
#
# # 第二步：读取数据
# content = file.read()  # 表示一次性读取文件中的所有数据
# print(content, type(content))
# # bytes： 字节类型
# # 第三步: 关闭文件
# file.close()


# rb模式读取文本文件中的数据-----------------------
file = open("test.txt", "rb")

# 第二步：读取数据
content = file.read()  # 表示一次性读取文件中的所有数据
print(content, type(content))
# 扩展：把字节数据转成字符串数据，其实就是对字节数据进行解码转成字符串数据
result = content.decode("utf-8")
print(result, type(result))
# 第三步: 关闭文件
file.close()

# rb的注意点：
# 1. 操作的文件必须存在
# 2. rb模式不需要再指定encoding这个参数

# 总结：rb模式可以兼容读取多种文件类型的数据
