# ab模式：以二进制或者字节的方式追加写入数据，在原文件数据的末尾追加写入新的数据

# 第一步：打开文件
file = open("5.txt", "ab")
# 第二步: 写入数据到文件
content = "你好"
# 对字符串进行编码，把字符串转成二进制或者字节
data = content.encode("utf-8")
print(data, type(data))
file.write(data)
# 第三步：关闭文件
file.close()

# ab模式的注意点：
# 1. 操作的文件不存在会创建一个空的文件，然后追加写入数据
# 2. 操作的文件存在，那么会在原文件的基础上追加写入数据，原文件中的数据保留

# 到目前为止我们操作文件的模式学习6种:
# 1. r
# 2. rb
# 3. w
# 4. wb
# 5. a
# 6. ab

# 了解: r+, rb+, w+, wb+, a+, ab+, 提示：带有加号的模式表示可以读写数据


# 练习题：实现图片的拷贝，把1.png图片进行拷贝，拷贝后的名字是2.png

# 作业题：[("李四", 20, "男"), ("貂蝉", 22, "女")]， 使用列表推导式
my_list = [("李四", 20, "男"), ("貂蝉", 22, "女")]
result = [{"name": my_tuple[0], "age": my_tuple[1], "sex": my_tuple[2]} for my_tuple in my_list]

print(result)

# 创建字典使用关键字方式进行传参
result = [dict(name=my_tuple[0], age=my_tuple[1], sex=my_tuple[2]) for my_tuple in my_list]

print(result)
