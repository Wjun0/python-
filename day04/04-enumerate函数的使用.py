# enumerate函数：使用for循环遍历数据时，既要数据的下标又要数据就可以结合enumerate函数来使用了
# enumerate函数经常结合容器类型(字符串，range，列表，元组，字典)使用

my_str = "hello"
for index, value in enumerate(my_str): # enumerate函数结合容器类型使用，遍历的每项数据是一个元组
    print(index, value)

print("------------------------")

for index, value in enumerate(range(1, 5)):
    print(index, value)

print("------------------------")

person_dict = {'name': '曹丕', 'age': 49, 'sex': '男'}

for index, item in enumerate(person_dict.items()):

    if index == 1:
        break

    # print(index, item)
    # 利用拆包，获取每项数据中的key和value
    key, value = item
    print(index, key, value)

