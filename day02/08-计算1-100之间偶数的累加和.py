# 计算1-100之间偶数的累加和

# 1. 生成1到100之间的每一个数字
num = 1
result = 0 # 记录所有偶数的累加和
while num <= 100:

    # 2. 判断生成的数字是否是偶数
    if num % 2 == 0:
        # 3. 把每一个偶数累加起来
        print(num)
        result += num
        print("result:", result)

    num += 1

print("偶数和的结果为:", result)



