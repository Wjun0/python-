# 计算1~100的累加和

# 1. 利用while循环把1到100之间的数字生成出来
num = 1
result = 0 # 累计和的结果
while num <= 100:
    # print(num)
    # 2. 把1-100之间的每一个数字加起来
    result += num
    # print("result:", result)
    num += 1

# 循环结束，表示结果计算完成
print("结果为:", result)
print("--------------")
num = 100
result = 0
while num >= 1:
    print(num)
    result += num
    num -= 1
print(result)