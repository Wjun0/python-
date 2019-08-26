# 导入模块
import random

# 1. 接收用户输入的拳, 石头(1)、剪刀(2)、布(3)
player = int(input("请出拳 石头(1)、剪刀(2)、布(3):"))
# 2. 让电脑随机出拳，范围[1-3]
computer = random.randint(1, 3)
print("computer:", computer)
# 3. 比较胜负，胜负结果有三种情况，1. 你赢了，2. 平局 3. 你输了
if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("你赢了")
elif player == computer:
    print("平局")
else:
    print("你输了")
