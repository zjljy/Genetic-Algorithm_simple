import random
from random import choices

N = 5  # 迭代次数
N1=N
bianyicishu = 0  # 统计变异次数
li = choices(range(32), k=4)  # 产生4个大于等于0小于等于31的随机整数，li是初始种群
print('初始种群为：',li)

def weight(x1, x2, x3, x4):  # 计算每个个体权重
    global weight1, weight2, weight3, weight4
    if x1 + x2 + x3 + x4 != 0:
        weight1 = x1**2 / (x1**2 + x2**2 + x3**2 + x4**2)
        weight2 = x2**2 / (x1**2 + x2**2 + x3**2 + x4**2)
        weight3 = x3**2 / (x1**2 + x2**2 + x3**2 + x4**2)
        weight4 = x4**2 / (x1**2 + x2**2 + x3**2 + x4**2)
    else:  # 如果x1,x2,x3,x4全为零
        weight1, weight2, weight3, weight4 = 0.25, 0.25, 0.25, 0.25

def change(x, y, place):  # 交换整数x和整数y对应二进制第place位到最后一位的内容（最多5位）
        global x1, y1

        x1 = list(map(int, bin(x).replace('0b', '')))  # bin用于获取整数对应二进制
        for i in range(1, 5 - len(x1) + 1):
            x1.insert(0, 0)

        y1 = list(map(int, bin(y).replace('0b', '')))
        for i in range(1, 5 - len(y1) + 1):
            y1.insert(0, 0)

        while place <= 4:
            x1[place], y1[place] = y1[place], x1[place]
            place += 1

        x1 = 16 * x1[0] + 8 * x1[1] + 4 * x1[2] + 2 * x1[3] + x1[4]  # 二进制转为整数
        y1 = 16 * y1[0] + 8 * y1[1] + 4 * y1[2] + 2 * y1[3] + y1[4]


while N > 0:
    N -= 1
    print('第%d次迭代'%(N1-N))

    weight(li[0], li[1], li[2], li[3])  # 计算每个个体权重
    print('当前种群内每个个体的适应度',[weight1,weight2,weight3,weight4])
    # 选择个体
    wei={0:weight1,1:weight2,2:weight3,3:weight4}
    wei=sorted(wei.items(),key=lambda item:item[1])

    gailv = [random.random(), random.random(), random.random(), random.random()]  # random.random()产生大于等于0小于1的随机数
    print('通过随机产生的概率所处区间进行选择，随机产生的概率为：', gailv)
    choose = [0, 0, 0, 0]  # choose[i]表示第i个个体选几个

    for i in range(4):
        if 0 <= gailv[i] < wei[0][1]:
            choose[wei[0][0]] += 1
        elif wei[0][1] <= gailv[i] < wei[0][1] + wei[1][1]:
            choose[wei[1][0]] += 1
        elif wei[0][1] + wei[1][1] <= gailv[i] < wei[0][1] + wei[1][1] + wei[2][1]:
            choose[wei[2][0]] += 1
        elif wei[0][1] + wei[1][1] + wei[2][1] <= gailv[i] < 1:
            choose[wei[3][0]] += 1

    print('当前每个个体对应的选择个数为：',choose,end=',')
    li = [li[0]] * choose[0] + [li[1]] * choose[1] + [li[2]] * choose[2] + [li[3]] * choose[3]
    print('对应选择后种群内的个体为：',li)


    if random.random() < 0.5:  # 变异,这里取50%明显点
        bianyicishu += 1
        place1 = random.randint(0, 4)  # 产生大于等于零小于等于4的整数
        place2 = random.randint(0, 4)
        print('发生了变异！随机选择的变异位置为第%d位和第%d位'%(place1,place2),end=',')
        change(li[0], li[1], place1)
        li[0] = x1
        li[1] = y1

        change(li[2], li[3], place2)
        li[2] = x1
        li[3] = y1
        print('变异后种群内个体为：',li)

print('共迭代了%d次，其中共变异了%d次' % (N1,bianyicishu))
print('种群当前个体：', li)
print('当前最优个体：', max(li))
