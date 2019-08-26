my_list = [1, 3, 0, 5]
print(my_list)
# 对列表数据进行排序, 默认是升序
# 错误写法
# result = my_list.sort()
# print(result)

# 排序方法
# my_list.sort()
# print(my_list)
#
# # 对列表数据进行反转, 排序方式改成降序
# my_list.reverse()
# print(my_list)

# 排序加反转的操作
my_list.sort(reverse=True)
print(my_list)

my_list = ["c", "a", "b"]
print(my_list)
# reverse:表示是否反转，True反转，False不反转
my_list.sort(reverse=True)
print(my_list)