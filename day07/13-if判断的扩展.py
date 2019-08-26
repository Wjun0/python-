# 1. if结合bool类型使用
# 2. if结合容器类型使用
# 3. if结合数字类型使用
# 4. if结合None类型使用

# 1. if结合bool类型使用， True表示条件成立， False表示条件失败
if False:
    print("ok")
else:
    print("error")

# 2. if结合容器类型使用, 容器类型(字符串，元组，字典，列表，集合，range，字节类型(bytes))中有数据表示条件成立，否则表示条件失败

my_str = ""
if my_str:
    print("条件成立")
else:
    print("条件不成立")

my_range = range(0)  # 此时range范围没有数据
if my_range:
    print("条件成立")
else:
    print("条件不成立")

my_bytes = b''  # 这里不要放汉字
if my_bytes:
    print("条件成立")
else:
    print("条件不成立")

# 3. if结合数字类型使用, 非零即真，如果是数字类型只要不是0就是真的(条件成立)
my_num = 1.5
if my_num:
    print("条件成立")
else:
    print("条件不成立")

# 4. if结合None类型使用, not None 表示条件成立，None表示条件不成立
my_value = None

if not my_value:
    print("条件成立")
else:
    print("条件不成立")

my_bytes = '哈哈'.encode("utf-8")
print(my_bytes)

if my_bytes:
    print("吼吼")