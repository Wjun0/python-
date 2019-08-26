# 1. read方法
# 1.1 read方法如果没有传入参数，表示把文件中的所有数据读取出来
# 1.1 read(数据长度)
# 1.1.1 如果打开文件的操作模式是r模式，这里的数据长度指定的字符串的数据长度
# 1.1.2 如果打开文件的操作模式是rb模式，这里的数据长度指定的字节的数据长度

# readline方法： 读取文件中的一行数据，默认从第一行

# readlines方法：读取文件中的所有行

# r模式读取数据----------
# file = open("5.txt", "r", encoding="utf-8")
# # 读取指定长度的文件数据, 这里的5表示5个字符串数据的长度
# content = file.read(5)
# print(content)
# file.close()

# rb模式读取数据--------
# file = open("5.txt", "rb")
# # 读取指定长度的文件数据， 这里的3表示3个字节的数据长度
# # 提示： 在utf-8编码格式下，一个汉字占用3个字节，一个字母或者数字占用1个字节
# content = file.read(3)
# print(content, type(content))
# result = content.decode("utf-8")
# print(result)
# file.close()

# readline方法的使用-------
# file = open("5.txt", "r", encoding="utf-8")
# # 读取一行数据
# content = file.readline()
# print(content)
# # 读取一行数据
# content = file.readline()
# print(content)
# file.close()

# readlines方法的使用

# file = open("5.txt", "r", encoding="utf-8")
# # 读取一行数据
# content = file.readlines()
# print(content)
#
# for row in content:
#     print(row)
#
# file.close()

# 总结： read(参数)使用的比较多

file = open("5.txt", "r", encoding="utf-8")
# 读取指定长度的文件数据, 这里的5表示5个字符串数据的长度
content = file.read(2)
print(content)
content = file.read(2)
print(content)
file.close()