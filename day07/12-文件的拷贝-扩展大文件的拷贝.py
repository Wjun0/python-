# 原文件的名字
src_file_name = "test.txt"

# 根据原文件名字生成拷贝后的文件名: test[复件].txt
# 1. 切片
# 2. split
# 3. partition 使用这种方式
file_name, point_str, end_str = src_file_name.partition(".")
dst_file_name = file_name + "[复件]" + point_str + end_str
print(dst_file_name)

# 1. 打开目标文件(拷贝后的文件)，目的就是创建一个空的文件
# 指定wb模式可以兼容文本文件和其他类型的文件(图片，视频，音频等等)
dst_file = open(dst_file_name, "wb")
# 2. 打开原文件，读取原文件中的数据
src_file = open(src_file_name, "rb")
# 拷贝大文件，不能一次性读取文件中的所有数据并加载到内存，可能导致内存暴涨及内存溢出
# data = src_file.read()

# 解决办法: 循环读取文件中的数据，每次加载一部分数据

while True:
    data = src_file.read(1024)  # 每次读取的最大字节长度
    # 查看每次读取到的数据和数据的长度
    print(data, type(data), len(data))
    # if len(data) > 0:
    # 判断字节类型是否有字节数据
    # 字节类型数据属于容器类型，好比字符串一样
    if data:
        # 3. 把原文件中的数据写入到目标文件里面
        dst_file.write(data)
    else:
        print("数据读取完成")
        break

# 4. 关闭文件
src_file.close()
dst_file.close()
