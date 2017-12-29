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


