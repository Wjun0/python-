# 提示：在python3.6之前dict类型的字典是无序的，想要使用有序的字典使用OrderDict类型
# 提示: 在python3.6及以后版本dict类型已经变成有序的
from collections import OrderedDict  # 从collections这个包里面导入OrderedDict类

my_dict = dict()  # 空的字典
my_dict["name"] = "刘备"
my_dict["age"] = 50
my_dict["sex"] = "男"
my_dict["address"] = "河北"

print(my_dict)

print("-------------------")

# 创建有序的字典
my_order_dict = OrderedDict() # 创建空的有序字典
# 添加键值对操作
my_order_dict["name"] = "刘备"
my_order_dict["age"] = 50
my_order_dict["sex"] = "男"
my_order_dict["address"] = "河北"

for key, value in my_order_dict.items():
    print(key, value)

# 测试：在python3.6及以后版本，查看dict类型是否是一个有序的字典
print("-----------在python3.6测试dict是否是有序的字典------------")
my_dict = dict()  # 空的字典
my_dict["name"] = "刘备"
my_dict["age"] = 50
my_dict["sex"] = "男"
my_dict["address"] = "河北"

print(my_dict)