# 遍历容器类型中的每一个数据，可以使用for循环来完成，因为比较方便和简单

my_str = 'abc'
for value in my_str:
    # 依次打印每次获取的数据
    print(value)

# for 结合range 获取字符串中的每一个数据
# 获取字符串的长度: len(字符串)
for index in range(len(my_str)):
    print(index, my_str[index])

# while循环
index = 0
while index < len(my_str):
    print(index, my_str[index])
    index += 1

print("-----------------------")

my_list = ["A", "B", "C"]

for value in my_list:
    print(value)

print("-----------------------")
index = 0
while index < len(my_list):
    print(index, my_list[index])
    index += 1

# 总结：想要获取容器类型中的每个数据，可以使用for循环来完成

my_str = "a b\tc\nd"
# 不指定参数，默认使用空白字符进行分割，空白字符：空格，\t, \n
result = my_str.split()
print(result)

