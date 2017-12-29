# 例2：
# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，
# 奖金可提10%；利润高于10万元，
# 低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可提成7.5%；20万到40万之间时，
# 高于20万元的部分，可提成5%；40万到60万之间时
# 高于40万元的部分，可提成3%；60万到100万之间时，
# 高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
# 程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
# 方法1：列表
# i = int(input('净利润')
# Bonus = [1000000,count=0
 #利润
# Bonuslist = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1] #利润对应利率
# count = 0 #计数器
# for idem in range(0, len(Bonus)):
#     if i > Bonus[idem]:  #大于奖励金额
#         count += (i - Bonus[idem]) * Bonuslist[idem]  #计算 count+本金*提成
#         print((i - Bonus[idem]) * Bonuslist[idem]) #打印每个层次得到提成
#         i = Bonus[idem]
# print (count) #提成
count=0
BonusList=[[100,0.01],[60,0.15],[40,0.03],[20,0.05],[10,0.075],[0,0.1]]
Profit= 210000
Profit /=10000
for i in range(0,len(BonusList)):
    if Profit > BonusList[0]:
        count += (Profit - BonusList[0])* BonusList[1]
        Profit = BonusList[0]
        #print(Profit)
print(count * 10000)
