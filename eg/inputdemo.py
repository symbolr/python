i = int(input('请输入利润>>>'))
Bonus = [1000000, 600000, 400000, 200000, 100000, 0] #利润
Bonuslist = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1] #利润对应利率
count = 0 #计数器
for idem in range(0, len(Bonus)):
    if i > Bonus[idem]:  #大于奖励金额
        count += (i - Bonus[idem]) * Bonuslist[idem]  #计算 count+本金*提成
        print((i - Bonus[idem]) * Bonuslist[idem]) #打印每个层次得到提成
        i = Bonus[idem]
print (count) #提成