# r模式：以字符串的方式读取文件中的数据

# 第一步：打开文件, 默认是在当前工程目录里面去找对应的文件
# 1. 要打开的文件
# 2. 文件的操作模式，默认是r模式
file = open("test.txt", "r", encoding="utf-8")
# 查看打开文件后的编码格式
# cp936其实就是GBK编码格式
print(file.encoding)
# 第二步：读取数据
content = file.read()  # 表示一次性读取文件中的所有数据
print(content, type(content))
# 第三步: 关闭文件
file.close()


# r模式的注意点：
# 1. 操作的文件必须存在，否则就崩溃
# 2. 在window的python解释器下，打开文件默认使用的gbk，在mac和liunx的python解释器下，打开文件默认使用utf-8
