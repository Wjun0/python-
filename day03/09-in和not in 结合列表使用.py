# in: 判断数据是否在列表里面
# not in: 判断数据不在列表里面

name_list = ["宋江", "晁盖", "阮小二"]

# 接收用户的姓名
name = input("请输入您要查询的姓名:")

result = name in name_list

print(result)

result = name not in name_list

print(result)