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
data = src_file.read()
# 3. 把原文件中的数据写入到目标文件里面
dst_file.write(data)
# 4. 关闭文件
src_file.close()
dst_file.close()
