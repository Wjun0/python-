# 列表嵌套：在列表里面再次使用列表

# 城市列表
city_list = []

# 北方城市列表
north_list = ["北京", "西安"]

# 南方城市列表
south_list = ["上海", "广州"]

# 把南方和北方城市列表添加到城市列表里面
city_list.append(north_list)
city_list.append(south_list)

print(city_list)

# 定义嵌套的列表
my_list = [['北京', '西安'], ['上海', '广州']]

# north_list = my_list[0]
# city_name = north_list[1]
#
# print(city_name)

# 简写方式
city_name = my_list[0][1]

print(city_name)

city_name = my_list[1][1]

print(city_name)
