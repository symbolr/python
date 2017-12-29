# 例1：
# 有四个数字：1、2、3、4能组成多少个互不相同且无重复的数字的三位数？各是多少？
# 审题：
# 1.去重
# 2.计算总数
# 方法1：
# dict =[]
# for  i in range(1,5):
# 	for j in range(1,5):
# 		for k in range(1,5):
# 			if i != j and i != k and j != k:
# 				dict.append([i,j,k])
# print("总数量:",len(dict))
# print(dict)
# # 方法2：
# num=[1,2,3,4]
# count=0
# for x in num:
#     for y in num:
#         for z in num:
#             if x != y and x != z and y != z:
#                 count +=1 #循环一次累计一次
#                 print(x,y,z)
# print("总数是>>>",count)
# # 方法3：整合for与if
# list_num = [1,2,3,4]
# list = [x*100 + y*10 + z*1 
# for x in list_num 
# for y in list_num 
# for z in list_num 
# if (x != y) and (x != z) and ( y != z)]
# print(list,len(list)) #打印不重复三位数及总数

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
